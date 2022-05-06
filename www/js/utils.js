(function () {
  function encodePostData (data) {
    return Object.keys(data).map(function (key) {
      var value = data[key]
      if (value === undefined) value = ''
      return key + '=' + encodeURIComponent(value)
    }).join('&')
  }

  function getCsrf () {
    return document.cookie.replace(/(?:(?:^|.*;\s*)csrftoken\s*=\s*([^;]*).*$)|^.*$/, '$1')
  }

  function post (url, data) {
    return fetch(url, {
      method: 'POST',
      body: encodePostData(data),
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': getCsrf()
      }
    })
  }

  function ajaxSubmit (form) {
    var data = {}
    var formData = new FormData(form)
    for (var pair of formData.entries()) {
      data[pair[0]] = pair[1];
    }
    return post(form.action, data)
  }

  function clearSelection() {
    if(document.selection && document.selection.empty) {
        document.selection.empty()
    } else if(window.getSelection) {
        var sel = window.getSelection()
        sel.removeAllRanges()
    }
  }

  function collapseSelection () {
    var sel = window.getSelection()
    if (sel.rangeCount) {
      var range = sel.getRangeAt(0)
      range.collapse()
      sel.removeAllRanges()
      sel.addRange(range)
    }
  }

  function setupEverything () {
    window.Utils = {
      post: post,
      ajaxSubmit: ajaxSubmit,
      clearSelection: clearSelection,
      collapseSelection: collapseSelection,
      setItemToLocal: function (key, value) {
        localStorage.setItem(key, JSON.stringify(value))
      },
      getItemFromLocal: function (key) {
        return JSON.parse(localStorage.getItem(key))
      }
    }
  }
  setupEverything()
})()
