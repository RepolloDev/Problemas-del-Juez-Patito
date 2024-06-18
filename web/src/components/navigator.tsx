import { component$ } from "@builder.io/qwik";
import Link from "./anchor-fix";
import {
  GoMarkGithub16,
  GoHome16,
  GoFileDirectory16,
  GoTag16,
} from "@qwikest/icons/octicons";

export default component$(() => {
  return (
    <header class="border-b-[1px] border-[#31373e] flex gap-5 py-4 items-center top-0 sticky bg-[#010409]">
      <div>
        <Link href="/" class="font-bold">
          JProblemas
        </Link>
      </div>
      <nav class="mx-auto">
        <ul class="flex gap-5 list-none">
          <li class="flex items-center">
            <Link href="/" class="hover:text-[#c3c4c6]">
              <GoHome16 class="w-4 h-4 text-[#c3c4c6] md:hidden" />
              <span class="hidden md:inline">Inicio</span>
            </Link>
          </li>
          <li class="flex items-center">
            <Link href="/problemas" class="hover:text-[#c3c4c6]">
              <GoFileDirectory16 class="w-4 h-4 text-[#c3c4c6] md:hidden" />
              <span class="hidden md:inline">Problemas</span>
            </Link>
          </li>
          <li>
            <Link href="/tags" class="hover:text-[#c3c4c6]">
              <GoTag16 class="w-4 h-4 text-[#c3c4c6] md:hidden" />
              <span class="hidden md:inline">Tags</span>
            </Link>
          </li>
        </ul>
      </nav>
      <div>
        <a href="https://github.com/RepolloDev/Problemas-del-Juez-Patito">
          <GoMarkGithub16 class="hover:text-[#c3c4c6] w-5 h-5" />
        </a>
      </div>
    </header>
  );
});
