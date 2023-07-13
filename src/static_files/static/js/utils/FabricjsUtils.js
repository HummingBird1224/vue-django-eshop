import { fabric } from "fabric";
import {jsPDF} from "jspdf";
import ImageUtils from './ImageUtils'
export default class FabricjsUtils {

  static applyFabricjsSetting() {
    fabric.Object.prototype.lockRotation = true;
    fabric.Object.prototype.lockSkewingY = true;
    fabric.Object.prototype.lockSkewingX = true;
    fabric.Object.prototype.lockUniScaling = true;
    fabric.Object.prototype.lockScalingFlip = true;
    fabric.Object.prototype.lockScalingFlip = true;
    fabric.Object.prototype.cornerColor = "#FFFFFF";
    fabric.Object.prototype.cornerStyle = "rectangle";
    fabric.Object.prototype.transparentCorners = false;
    fabric.Object.prototype.cornerStrokeColor = "#205EFB";
    fabric.Object.prototype.setControlVisible("mb", false);
    fabric.Object.prototype.setControlVisible("ml", false);
    fabric.Object.prototype.setControlVisible("mr", false);
    fabric.Object.prototype.setControlVisible("mtr", false);
    fabric.Object.prototype.setControlVisible("mt", false);
  }

  // Fabricのコントロールを生成する
  static createRenderingIconFunction(imgSource, imageSize) {
    const img = document.createElement('img');
    img.src = imgSource;
    return function (ctx, left, top, _, fabricObject) { // arrowじゃなくてfunctionにしているのは意図的
      ctx.save();
      ctx.translate(left, top);
      ctx.beginPath();
      ctx.arc(0, 0, 12, 0, Math.PI*2, false); // 白い円を描く
      ctx.fill();　// 塗る
      ctx.rotate(fabric.util.degreesToRadians(fabricObject.angle));
      ctx.drawImage(img, - imageSize/ 2, -imageSize/2, imageSize, imageSize); // 画像のレンダリング
      ctx.restore();
    };
  }

  static setupDeletingObjectControl(control_number, deletingFunction) {
    const deleteIcon = "data:image/svg+xml;charset=utf8,%3Csvg%20width%3D%2212%22%20height%3D%2215%22%20viewBox%3D%220%200%2012%2015%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20fill-rule%3D%22evenodd%22%20clip-rule%3D%22evenodd%22%20d%3D%22M7.91667%200L8.75%200.833333H11.6667V2.5H0V0.833333H2.91667L3.75%200H7.91667ZM0.833133%2013.3333C0.833133%2014.25%201.58313%2015%202.4998%2015H9.16647C10.0831%2015%2010.8331%2014.25%2010.8331%2013.3333V3.33332H0.833133V13.3333ZM2.49984%205H9.1665V13.3333H2.49984V5Z%22%20fill%3D%22black%22%2F%3E%3C%2Fsvg%3E";
    return new fabric.Control({
      x: 0.5,
      y: -0.5,
      offsetY: 14*(2*control_number + 1),
      offsetX: 24,
      cursorStyle: 'pointer',
      mouseUpHandler: deletingFunction,
      render: FabricjsUtils.createRenderingIconFunction(deleteIcon, 12),
      cornerSize: 24
    });
  }

  static setupTypographyPaneControl(control_number, showTypographyPaneFunction) {
    const typographyIcon = "data:image/svg+xml,%3Csvg width='16' height='16' viewBox='0 0 16 16' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M15.5385 13.0769H14.2282L9.57906 0.303688C9.51272 0.121344 9.33938 0 9.14538 0H6.85463C6.66059 0 6.48731 0.121344 6.42091 0.303688L1.77184 13.0769H0.461531C0.206656 13.0769 0 13.2836 0 13.5385V15.5385C0 15.7933 0.206656 16 0.461531 16H6.15384C6.40875 16 6.61538 15.7933 6.61538 15.5385V13.5385C6.61538 13.2836 6.40872 13.0769 6.15384 13.0769H4.88253L5.66647 10.9231H10.3336L11.1175 13.0769H9.84616C9.59125 13.0769 9.38463 13.2836 9.38463 13.5385V15.5385C9.38463 15.7934 9.59128 16 9.84616 16H15.5385C15.7934 16 16 15.7933 16 15.5385V13.5385C16 13.2836 15.7933 13.0769 15.5385 13.0769ZM6.67434 8.15384L8 4.51169L9.32566 8.15384H6.67434Z' fill='black'/%3E%3C/svg%3E%0A";
    return new fabric.Control({
      x: 0.5,
      y: -0.5,
      offsetY: 14*(2*control_number + 1),
      offsetX: 24,
      cursorStyle: 'pointer',
      mouseUpHandler: showTypographyPaneFunction,
      render: FabricjsUtils.createRenderingIconFunction(typographyIcon, 14),
      cornerSize: 24
    });
  }


  static setupVerticalAlignmentObjectControl(control_number) {
    const verticalIcon = "data:image/png;base64,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";
    return new fabric.Control({
      x: 0.5,
      y: -0.5,
      offsetY: 14*(2*control_number + 1),
      offsetX: 24,
      cursorStyle: 'pointer',
      mouseUpHandler: FabricjsUtils.alignVerticalCenter,
      render: FabricjsUtils.createRenderingIconFunction(verticalIcon, 14),
      cornerSize: 24
    });
  }

  static setupHorizontalAlignmentObjectControl(control_number) {
    const horizontalIcon = "data:image/png;base64,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";
    return new fabric.Control({
      x: 0.5,
      y: -0.5,
      offsetY: 14*(2*control_number + 1),
      offsetX: 24,
      cursorStyle: 'pointer',
      mouseUpHandler: FabricjsUtils.alignHorizontalCenter,
      render: FabricjsUtils.createRenderingIconFunction(horizontalIcon, 14),
      cornerSize: 24
    });
  }

  static setupBringFrontControl(control_number) {
    const bringFront = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABYlAAAWJQFJUiTwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAFGSURBVHgB7Zg9bsJAEIUfSZoUSZBSJ0Lp0qVLS06QIgcIR+AIHIEb4CNATcMBKIAD8NOARIGgoAEJmBFYWq0wu2vvyC72k97KO4O1I3seXrsEdz5I7/DPhDSDI2XShnQUUJ8XuIMbXNAzZHjl4QHp+YEf6qTfeJKloB78UFMnrrdMnFtX6JP0p/2mrBw3kI41qYkUDCDjJtabsk50iU14cuuWvUCO+6SETQ9FpJInGSlcUxfWZeymJy0XO6oC7b/CkgOpS1rAkSrk3PSvrRXHK0osgqXLfGDVyCqhqU2EgkyEgkxk2aBloaUcf6mJvAqqXontecirIN5Hb7TYmIe8CuqQptcSwWUmpAtiN6lPfyN5XaFdUkK6qdukoRZbkuZJJ0gXxG6KXE4ILjNRyIJWsLRkCrZwJN6Ef5Me4Rd+DRrh/HHBmhM0uWuxgqWFgAAAAABJRU5ErkJggg==";
    return new fabric.Control({
      x: 0.5,
      y: -0.5,
      offsetY: 14*(2*control_number + 1),
      offsetX: 24,
      cursorStyle: 'pointer',
      mouseUpHandler: FabricjsUtils.bringFront,
      render: FabricjsUtils.createRenderingIconFunction(bringFront, 14),
      cornerSize: 24
    });
  }

  static setupBringBackControl(control_number) {
    const bringBack = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAADKSURBVHgBtZK9DcIwEIVfIANQ0MMGqSlQoGIJJIIYgJ7KWQOxAQ0lHaKiDZuwAdwJW7IsnxPn50mf5NNzXnK5SyDrQozRTOckYH7RXOUIPSl16isxRQu5rXE7N+Jd81xOrKy6hCeoQL2UvmtQ3NqB2FqXjsROCHgRJ5/BQUt9fmokZcRCMlMrRCGsAvKXorfxD7ZHMfoQlT5XXYJ43/amiG1tjv9QcteIDZpYIQ/biG2N/8naZ5ggfotCWFnI5KA7sSFmCIunJG7+DxXyHdciNFk8AAAAAElFTkSuQmCC";
    return new fabric.Control({
      x: 0.5,
      y: -0.5,
      offsetY: 14*(2*control_number + 1),
      offsetX: 24,
      cursorStyle: 'pointer',
      mouseUpHandler: FabricjsUtils.bringBack,
      render: FabricjsUtils.createRenderingIconFunction(bringBack, 14),
      cornerSize: 24
    });
  }

  static bringFront(_, event, positon) {
    const { target } = event;
    const { canvas } = target;
    canvas.bringToFront(target);
    canvas.requestRenderAll()
  }

  static bringBack(_, event, position) {
    const { target } = event;
    const { canvas } = target;
    canvas.sendToBack(target)
    canvas.requestRenderAll()
  }

  static alignHorizontalCenter(_, event, position) {
    const { target } = event;
    const { canvas } = target;
    const { x } = target.aCoords.tl;
    const { x: edgeX } = target.aCoords.br;
    const operatedWidth = edgeX - x;
    target.left = canvas.width/2 - operatedWidth/2;
    target.setCoords();
    canvas.requestRenderAll()
  }

  static alignVerticalCenter(_, event, position) {
    const { target } = event;
    const { canvas } = target;
    const { y } = target.aCoords.tl;
    const { y: edgeY } = target.aCoords.br;
    const operatedHeight = edgeY - y;
    target.top = canvas.height/2 - operatedHeight/2;
    target.setCoords();
    canvas.requestRenderAll()
  }

  static removeObject(target) {
    const { canvas } = target;
    canvas.remove(target);
  }

  static drawGrid(canvas, color, grid, strokeWidth = 1) {
    const grids = []
    // draw horizontal lines
    for(let x = 0; x < canvas.width/grid; x++) {
        const line = new fabric.Line([ 0, x * grid, canvas.width, x * grid], { type: 'line', stroke: color, selectable: false, strokeWidth: strokeWidth });
        canvas.add(line);
        grids.push(line)
    }

    // draw vertical lines
    for(let y = 0; y < canvas.width/grid; y++) {
        const line =new fabric.Line([ y * grid, 0, y * grid, canvas.height], { type:'line', stroke: color, selectable: false, strokeWidth: strokeWidth })
        canvas.add(line);
        grids.push(line);
    }

    return grids;
  }

  static async processingPDF(canvases, printAreas, pdfWidth, pdfHeight, pdfColor, pdfBorder) {
    const scale = 72/ 25.4;

    if (pdfWidth >= pdfHeight) {
      var pdf = new jsPDF({
        orientation: "l",
        unit: "mm",
        format: [pdfWidth * scale, pdfHeight * scale],
      });
    } else {
      var pdf = new jsPDF({
        orientation: "p",
        unit: "mm",
        format: [pdfWidth * scale, pdfHeight * scale],
      });
    }

    pdf.setFillColor(pdfColor);
    pdf.setDrawColor(pdfBorder);
    pdf.rect(0, 0, pdfWidth, pdfHeight, "DF");
    for(let i = 0; i < canvases.length; i++) {
      if (printAreas[i].is_printable) {
        await FabricjsUtils.appendCanvasImageToPdf(canvases[i], printAreas[i].position.pdf, pdf)
      }
    }

     return pdf.output("blob");
  }

  static async appendCanvasImageToPdf(canvas, position, pdf) {

    const objects = FabricjsUtils.getinsertedObject(canvas);

    const { start, end } = position
    const imgWidth = end.x - start.x;
    const imgHeight = end.y - start.y;

    const width = canvas.getWidth();
    const height = canvas.getHeight();


    const image = await FabricjsUtils.generateCanvasImage(objects, width, height);
    pdf.addImage(image, "PNG", start.x, start.y, imgWidth, imgHeight); // 通常のサイズに縮小する

    // 線を引く
    pdf.line(start.x, start.y, end.x, start.y);
    pdf.line(start.x, start.y, start.x, end.y);
    pdf.line(end.x, start.y, end.x, end.y);
    pdf.line(start.x, end.y, end.x, end.y);
  }

  static getinsertedObject(canvas) {
    return canvas.getObjects().filter(o=>o.type != 'line' && o.type != 'object') ?? []
  }

  static async generateCanvasImage(objects, width, height, targetPpi = 300) {
    let icanvas = document.createElement("canvas")
    const context = icanvas.getContext("2d")

    const targetPpmm = targetPpi / 2.54/ 10;

    icanvas.width = width * targetPpmm
    icanvas.height = height * targetPpmm

    for(let i = 0; i < objects.length; i++) {
      await FabricjsUtils.applyObjectImage(objects[i], targetPpmm, context)
    }

    const dataURI = icanvas.toDataURL("image/png")

    return dataURI
  }

  // キャンバスの画像データを生成する
  static async applyObjectImage(object, targetPpmm, context) {
    const { x, y } = object.aCoords.tl;
    const { x: edgeX, y: edgeY } = object.aCoords.br;

    // スケールサイズを測定
    const operatedWidth = edgeX - x;
    const operatedHeight = edgeY - y;

    const { source, drawWidth, drawHeight, } = (function(object, targetPpmm, operatedHeight, operatedWidth) {
      switch (object.type) {

        case 'image':
          return {
            source: object._originalElement.currentSrc,
            drawWidth: object.width,
            drawHeight: object.height
          }
        case 'textbox':
          return {
            source: object.toDataURL({
              format: 'png',
              multiplier: targetPpmm
            }),
            drawWidth: operatedWidth * targetPpmm,
            drawHeight: operatedHeight * targetPpmm,
          }

      }
    })(object, targetPpmm, operatedHeight, operatedWidth);
    const loadImage = await ImageUtils.loadImage(source)
    context.drawImage(
      loadImage,
      0,
      0,
      drawWidth,
      drawHeight,
      x * targetPpmm,
      y * targetPpmm,
      operatedWidth * targetPpmm,
      operatedHeight * targetPpmm,
    )
  }
}
