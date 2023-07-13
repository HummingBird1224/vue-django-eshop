export default enName => {
  switch (enName) {
    case 'height':
      return '高さ';
    case 'width':
      return '幅';
    case 'depth':
      return '奥行き';
    case 'lip':
      return 'フタ';
    default:
      return enName;
  }
}
