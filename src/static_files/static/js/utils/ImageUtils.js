export default class ImageUtils {

  static isNearBlack(color) {
    return ImageUtils.isNearColorFunc([0, 0, 0])(color)
  }

  static isNearWhite(color) {
    return ImageUtils.isNearColorFunc([255, 255, 255])(color)
  }

  static isNearColorFunc(refColor) {
    const [refR, refG, refB] = refColor;
    return (color) => {
      const [r, g, b] = color;
      const thresholdDistance = 50;
      return (
        Math.abs(refR - r) < thresholdDistance &&
        Math.abs(refG - g) < thresholdDistance &&
        Math.abs(refB - b) < thresholdDistance
        );
    };
  }

  static loadImage(source) {
    return new Promise((resolve, reject) => {
      const img = new Image();
      img.onload = () => resolve(img);
      img.onerror = (e) => reject(e);
      img.src = source;
    });
  }
}
