import DraftFlow from "../constants/DraftFlow";

export default serverStateStr => {
  switch (serverStateStr) {
    case 'not_submitted':
      return DraftFlow.NOT_SUBMITTED;
    case 'under_check':
      return DraftFlow.UNDER_CHECK;
    case 'resubmission_request':
      return DraftFlow.RE_SUBMITTION_REQUEST;
    case 'checked':
      return DraftFlow.CHECKED;
    case 'unassigned':
    case 'printing':
      return DraftFlow.PRINTING;
    case 'shipped':
      return DraftFlow.SHIPPED;
    case 'delivered':
      return DraftFlow.DELIVERED;

    default:
      return null;
  }
};
