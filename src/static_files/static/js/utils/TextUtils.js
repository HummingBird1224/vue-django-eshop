export default class TextUtils {
  static truncateString(label, length) {

    if (label.length < length) return label;

    return label.substr(0, length) + '...';
  }

}
