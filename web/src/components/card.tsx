import { component$ } from "@builder.io/qwik";
import type { FileRead } from "~/data/types";
import { getLanguage } from "~/data/utils";
import Link from "./anchor-fix";
import Badge from "./badge";

export default component$<FileRead>((props) => {
  const { id, name, path, ext, tags } = props;
  const language = getLanguage(ext);
  return (
    <div class="card outline outline-1 outline-[#31373e] rounded-md p-4 flex flex-col gap-2 w-full">
      <div class="head flex gap-2 items-center">
        <span class="bg-slate-200 inline-block rounded-full overflow-hidden w-5 h-5">
          <img
            src={`https://api.dicebear.com/9.x/identicon/svg?seed=${id}?size=32`}
            width={32}
            height={32}
          />
        </span>
        <h3>
          <Link
            href={`problems/${id}`}
            class="underline text-blue-500 font-semibold text-sm md:text-base break-all"
          >
            {path}
          </Link>
        </h3>
      </div>
      <div class="body flex flex-col gap-2 my-auto">
        <span>{name}</span>
        <div class="flex gap-2 flex-wrap">
          {tags.map((tag, i) => (
            <Badge key={i} href={`/tags/${tag}`} text={tag} />
          ))}
        </div>
      </div>
      <div class="footer flex text-xs text-[#919ba5] gap-2 mt-auto">
        <span class="flex items-center gap-2">
          <span
            style={{
              backgroundColor: language.color,
            }}
            class="w-2 h-2 rounded-full inline-block"
          />
          <span class="capitalize">{language.name}</span>
        </span>
      </div>
    </div>
  );
});
