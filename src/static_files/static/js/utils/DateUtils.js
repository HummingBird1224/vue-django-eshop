export default class DateUtils {

  static millisecFormat(date) {
    return DateUtils.dateFormat(date, "yyyy-MM-dd-HH-mm-ss-SSS")
  }

  static dateFormat(date, format) {
    format = format.replace(/yyyy/g, date.getFullYear());
    format = format.replace(/MM/g, ("0" + (date.getMonth() + 1)).slice(-2));
    format = format.replace(/M/g, date.getMonth() + 1);
    format = format.replace(/dd/g, ("0" + date.getDate()).slice(-2));
    format = format.replace(/d/g, date.getDate());
    format = format.replace(/HH/g, ("0" + date.getHours()).slice(-2));
    format = format.replace(/mm/g, ("0" + date.getMinutes()).slice(-2));
    format = format.replace(/ss/g, ("0" + date.getSeconds()).slice(-2));
    format = format.replace(/SSS/g,("00" + date.getMilliseconds()).slice(-3));
    return format;
  }
}
