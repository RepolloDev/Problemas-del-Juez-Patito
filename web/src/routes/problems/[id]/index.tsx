import { component$ } from "@builder.io/qwik";
import {
  routeLoader$,
  type StaticGenerateHandler,
} from "@builder.io/qwik-city";
import { getAllFilesInfo, contentHtmlById } from "~/data";
import { getLanguage } from "~/data/utils";
import Badge from "~/components/badge";
import "remark-callouts/styles.css";

export const useData = routeLoader$(async (req) => {
  const id = parseInt(req.params.id);
  const content = await contentHtmlById(id);
  return content;
});

export default component$(() => {
  const { value } = useData();
  const { name, tags, content, path, url, ext } = value;
  const { description, steps, code } = content;
  const language = getLanguage(ext);
  return (
    <>
      <div class="flex flex-col gap-5 items-center w-full mb-5">
        <h1 class="mb-0">{name}</h1>
        <div class="w-1/2 flex flex-wrap justify-center gap-2">
          {tags.map((tag, i) => (
            <Badge key={i} href={tag} text={tag} />
          ))}
        </div>
        <div class="flex gap-5">
          <a
            href={`https://github.com/RepolloDev/Problemas-del-Juez-Patito/tree/main/${path}`}
            class="p-2 rounded-md bg-[#00aa34] hover:bg-[#29903b] font-bold text-sm"
          >
            Ver en GitHub
          </a>
          <a
            href={url}
            class="p-2 rounded-md bg-[#6c3cc4] hover:bg-[#7e44c8] font-bold text-sm"
          >
            Ver en el Juez
          </a>
        </div>
      </div>
      <article class="prose md:prose-lg prose-invert max-w-none">
        <div dangerouslySetInnerHTML={description} />
        <div dangerouslySetInnerHTML={steps} />
        <div class="outline outline-1 outline-[#333941] rounded-md flex flex-col prose-figure:m-0">
          <div class="flex items-center gap-2 p-2 bg-[#161b22]">
            <div class="flex items-center gap-2 p-2 rounded-md bg-black outline outline-1 outline-[#333941] capitalize">
              <span
                style={{
                  backgroundColor: language.color,
                }}
                class="w-2 h-2 block rounded-full"
              />
              <span>{language.name}</span>
            </div>
          </div>
          <div dangerouslySetInnerHTML={code} />
        </div>
      </article>
    </>
  );
});

export const onStaticGenerate: StaticGenerateHandler = async () => {
  const files = await getAllFilesInfo();
  return {
    params: files.map((file) => ({ id: file.id.toString() })),
  };
};
