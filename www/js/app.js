(function () {
  function getAllTaskIds () {
    var allTaskIds = []
    document.querySelectorAll('[data-task-id]').forEach(el => {
      allTaskIds.push(el.dataset.taskId)
    })
    return allTaskIds
  }

  function getNextTaskId (activeTaskId) {
    var allTaskIds = getAllTaskIds()
    var targetIdx = allTaskIds.indexOf(activeTaskId) + 1
    if (targetIdx >= allTaskIds.length) targetIdx = allTaskIds.length - 1
    return allTaskIds[targetIdx]
  }

  function getPreviousTaskId (activeTaskId) {
    var allTaskIds = getAllTaskIds()
    var targetIdx = allTaskIds.indexOf(activeTaskId) - 1
    if (targetIdx < 0) targetIdx = 0
    return allTaskIds[targetIdx]
  }

  function setFocus (taskId) {
    var task = document.querySelector(`[data-task-id="${taskId}"]`)
    task.focus()
  }

  function getSnoozeTime (number, units) {
    var now = new Date()
    var number = parseInt(number)
    switch (units) {
      case 'minutes':
        now.setMinutes(now.getMinutes() + number)
        break
      case 'hours':
        now.setHours(now.getHours() + number)
        break
      case 'days':
        now.setDate(now.getDate() + number)
        now.setHours(8)
        now.setMinutes(0)
        now.setSeconds(0)
        break
      case 'weeks':
        now.setDate(now.getDate() + number * 7)
        now.setHours(8)
        now.setMinutes(0)
        now.setSeconds(0)
        break
    }
    return now
  }

  function setupEverything () {
    window.App = {
      getNextTaskId: getNextTaskId,
      getPreviousTaskId: getPreviousTaskId,
      setFocus: setFocus,
      getSnoozeTime: getSnoozeTime
    }
  }
  setupEverything()
})()
