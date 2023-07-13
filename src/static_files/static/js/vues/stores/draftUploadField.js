import ApiManager from "../../helpers/ApiManager";
import toDraftFlow from "../../helpers/toDraftFlow";
import DraftFlow from "../../constants/DraftFlow";

class Store {
  constructor() {
    this.store = {};
  }

  getStore() {
    return this.store;
  }

  createStore($el) {
    this.store = {
      state: {
        refCode: $el.data("ref-code"),
        flow: toDraftFlow($el.data("state")),
        staticUrl: $el.data("static-url"),
        orderInfo: null,
        productInfo: null,
        isShowUploadModal: false,
        isShowCheckDraftModal: false,
        isShowEasyUploadModal: false,
        isFileUploading: false,
        isFileUploaded: false,
        uploadFileName: "",
        uploadFileId: "",
        uploadFileSize: "",
        uploadPercentCompleted: 0,
        uploadFileUrl: "",
      },
      clearUploadedData() {
        this.state.isFileUploading = false;
        this.state.isFileUploaded = false;
        this.state.uploadFileName = "";
        this.state.uploadFileId = "";
        this.state.uploadPercentCompleted = 0;
        this.state.uploadFileUrl = "";
      },
      setFlow(flow) {
        this.state.flow = flow;
      },
      openUploadModal() {
        this.state.isShowUploadModal = true;
      },
      closeUploadModal() {
        this.state.isShowUploadModal = false;
      },
      openEasyUploadModal() {
        this.state.isShowEasyUploadModal = true;
      },
      closeEasyUploadModal() {
        this.state.isShowEasyUploadModal = false;
      },
      openCheckDraftModal() {
        this.state.isShowCheckDraftModal = true;
      },
      closeCheckDraftModal() {
        this.state.isShowCheckDraftModal = false;
      },
      fetchOrderInfo() {
        return ApiManager.getDraftOrderInfo(this.state.refCode).then((res) => {
          this.setFlow(toDraftFlow(res.data.state));
          this.state.orderInfo = res.data;
        });
      },
      fetchProductInfo() {
        return ApiManager.getEasyDraftInfo(this.state.refCode).then((res) => {
          this.state.productInfo = res.data;
        });
      },
      resetUploadStatus() {
        this.state.isFileUploaded = false;
        this.state.isFileUploading = false;
      },
      postUploadFile(file) {
        this.state.isFileUploading = true;
        this.state.isFileUploaded = false;

        // ファイルアップの進行状況を　state.uploadPercentCompleted に代入.
        const onUploadProgress = (progressEvent) => {
          const percentCompleted = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );

          this.state.uploadPercentCompleted = percentCompleted;

          return percentCompleted;
        };

        // formDataのbuild.
        const formData = new FormData();

        formData.append("item_ref", this.state.refCode);
        formData.append("data", file);

        return ApiManager.postUploadDesign(
          this.state.refCode,
          formData,
          onUploadProgress
        )
          .then((res) => {
            if (this.state.flow === DraftFlow.UNDER_CHECK) {
              this.setFlow(DraftFlow.NOT_SUBMITTED);
            }

            this.state.uploadFileId = res.data.id;
            this.state.uploadFileUrl = res.data.data;
            this.state.uploadFileSize = res.data.size;
            this.state.isFileUploaded = true;
          })
          .finally(() => {
            this.state.isFileUploading = false;
          });
      },
      postEasyDraftUpload(file) {
        this.state.isFileUploading = true;
        this.state.isFileUploaded = false;

        // ファイルアップの進行状況を　state.uploadPercentCompleted に代入.
        const onUploadProgress = (progressEvent) => {
          const percentCompleted = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );

          this.state.uploadPercentCompleted = percentCompleted;
          return percentCompleted;
        };

        // formDataのbuild.
        const formData = new FormData();

        formData.append("item_ref", this.state.refCode);
        formData.append("data", file);

        return ApiManager.postEasyDraftUpload(
          this.state.refCode,
          formData,
          onUploadProgress
        )
          .then((res) => {
            if (this.state.flow === DraftFlow.UNDER_CHECK) {
              this.setFlow(DraftFlow.NOT_SUBMITTED);
            }

            this.state.uploadFileId = res.data.id;
            this.state.uploadFileUrl = res.data.data;
            this.state.uploadFileSize = res.data.size;
            this.state.isFileUploaded = true;
          })
          .finally(() => {
            this.state.isFileUploading = false;
          });
      },
      withDrawUploadedDesign() {
        return ApiManager.withdrawUploadedDraftData(this.state.refCode);
      },
      postConfirmUpload() {
        const formValue = {
          id: this.state.uploadFileId,
        };

        return ApiManager.postConfirmUpload(this.state.refCode, formValue);
      },
      postConfirmDesign() {
        return ApiManager.postConfirmDesign(this.state.refCode, {});
      },
    };

    return this.store;
  }
}

export default new Store();
