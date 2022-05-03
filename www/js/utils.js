(function () {
  function encodePostData (data) {
    return Object.keys(data).map(function (key) {
      var value = data[key]
      if (value === undefined) value = ''
      return key + '=' + encodeURIComponent(value)
    }).join('&')
  }

  function ajaxSubmit (form) {
    var data = {}
    var formData = new FormData(form)
    for (var pair of formData.entries()) {
      data[pair[0]] = pair[1];
    }
    // send POST request via fetch API
    return fetch(form.action, {
      method: 'POST',
      body: encodePostData(data),
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })
  }

  function setupEverything () {
    window.Utils = {
      ajaxSubmit: ajaxSubmit
    }
  }
  setupEverything()
})()
