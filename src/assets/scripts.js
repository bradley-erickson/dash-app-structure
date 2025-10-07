// assets/scripts.js
/**
 * 
 */
if (!window.dash_clientside) {
  window.dash_clientside = {};
}

window.dash_clientside.clientside = {
  toggleWithButton: function (clicks, isOpen) {
    if (clicks > 0) {
      return !isOpen;
    }
    return isOpen;
  },

  returnValue: function (value) {
    return value;
  }
}
