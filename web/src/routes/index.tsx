import { component$ } from "@builder.io/qwik";
import { routeLoader$, type DocumentHead } from "@builder.io/qwik-city";
import { readAllFiles } from "~/data";
import Card from "~/components/card";

export const useData = routeLoader$(async () => {
  const data = await readAllFiles();
  return data;
});

export default component$(() => {
  const { value } = useData();
  const data = value.slice(-10);

  return (
    <>
      <section>
        <h1 class="text-center">Problemas del Juez Patito 🔨🦆</h1>
        <img
          class="mb-5"
          src="https://github.com/RepolloDev/Problemas-del-Juez-Patito/blob/main/public/banner.png?raw=true"
          width={915}
          height={214}
        />
        <p class="prose prose-invert md:prose-xl">
          Este repositorio contiene la solución a los problemas del juez patito,
          una plataforma de problemas de la{" "}
          <i>Universidad Mayor de San Andrés</i>. Los problemas están resueltos
          únicamente en Python pero se dejan explicaciones detalladas de los
          problemas para que puedan ser resueltos en otros lenguajes de
          programación.
        </p>
      </section>
      <section>
        <h2>Últimos problemas</h2>
        <div class="flex flex-col gap-5 md:grid md:grid-cols-2">
          {data.map((item) => (
            <Card key={item.id} {...item} />
          ))}
        </div>
      </section>
    </>
  );
});

export const head: DocumentHead = {
  title: "Problemas Algortimicos",
  meta: [
    {
      name: "description",
      content:
        "Problemas de algoritmos resueltos en Python del juez virtual de la Universidad Mayor de San Andrés",
    },
  ],
};
