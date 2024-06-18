import { component$, type AnchorHTMLAttributes } from "@builder.io/qwik";
//import { base } from "../consts"
import { Slot } from "@builder.io/qwik";

interface LinkProps extends AnchorHTMLAttributes<HTMLAnchorElement> {
  href?: string;
}

export default component$<LinkProps>((props) => {
  const ref = props.href;
  return (
    <a {...props} href={ref}>
      <Slot />
    </a>
  );
});
