import { component$ } from "@builder.io/qwik";
import Link from "./anchor-fix";

interface BadgeProps {
  href: string;
  text: string;
}

export default component$<BadgeProps>(({ href, text }) => {
  return (
    <Link
      href={href}
      class="text-xs px-1 py-0.5 rounded-md bg-[#121d2f] text-blue-500 font-semibold hover:bg-blue-500 hover:text-slate-100"
    >
      {text}
    </Link>
  );
});
