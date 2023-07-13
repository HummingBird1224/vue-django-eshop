export default (start, end, step = 1) => Array.from({length: (end - start + step) / step}, (v, k) => start + k * step);
