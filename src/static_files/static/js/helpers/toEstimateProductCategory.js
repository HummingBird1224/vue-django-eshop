import EstimateProductCategory from "../constants/EstimateProductCategory";

export default categoryStr => {
  switch (categoryStr) {
    case 'flatbag':
      return EstimateProductCategory.FLAT_BAG;
    case 'cardboard':
      return EstimateProductCategory.CARD_BOARD;
    case 'paperbox':
      return EstimateProductCategory.PAPER_BOX;
    default:
      return EstimateProductCategory.FLAT_BAG;
  }
}
