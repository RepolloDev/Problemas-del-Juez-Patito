import { component$ } from "@builder.io/qwik";

export default component$(() => {
  return (
    <footer class="py-10">
      <div class="flex justify-center">
        Hecho con ❤️ por{" "}
        <a
          href="https://github.com/RepolloDev"
          class="underline text-blue-500 ml-1"
        >
          @RepolloDev
        </a>
      </div>
    </footer>
  );
});
