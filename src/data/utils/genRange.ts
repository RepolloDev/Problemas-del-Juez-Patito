/**
 * Generate a range of numbers in the form of [a, b].
 * This is relationated with the directories that contain the files.
 * @param index : index of the range to generate
 */
export function* genRange(index: number = 0): Generator<[number, number]> {
  const init = 1000;
  const step = 199;

  let [a, b] = [init + index * (step + 1), init + index * (step + 1) + step];
  while (true) {
    yield [a, b];
    a = b + 1;
    b = a + step;
  }
}
