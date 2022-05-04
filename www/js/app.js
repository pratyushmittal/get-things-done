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

  function setupEverything () {
    window.App = {
      getNextTaskId: getNextTaskId,
      getPreviousTaskId: getPreviousTaskId
    }
  }
  setupEverything()
})()
