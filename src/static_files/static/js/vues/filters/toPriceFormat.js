export default function toPriceFormat(value) {
  if (value !== 0 && !value) {
    return false;
  }
  return value.toString().replace(/([0-9]+?)(?=(?:[0-9]{3})+$)/g, '$1,');
}
