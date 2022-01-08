export default function useClasses(...classes: string[]) {
  return classes.reduce((prev: string, cur: string) => `${prev} ${cur}`);
}
