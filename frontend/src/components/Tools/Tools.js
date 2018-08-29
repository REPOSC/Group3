const MAX_VALUE = 12

function get_url() {
  return 'http://139.199.106.168:8000/'
}

function checkcount(number, saved) {
  if (!checknum(number, saved)) {
    return false
  }
  if (parseInt(number) >= 1000) {
    saved.$notify({
      title: '警告',
      message: '输入的数字过大，请检查！',
      type: 'warning'
    })
    return false
  } else if (parseInt(number) === 0) {
    saved.$notify({
      title: '警告',
      message: '这个数字不能为零！',
      type: 'warning'
    })
    return false
  }
  return true
}

function checknum(number, saved) {
  for (let i = 0; i < number.length; ++i) {
    if (number[i] > '9' || number[i] < '0') {
      saved.$notify({
        title: '警告',
        message: '输入的数字非法，请检查!',
        type: 'warning'
      })
      return false
    }
  }
  if (number.length === 0) {
    saved.$notify({
      title: '警告',
      message: '输入的数字非法，请检查!',
      type: 'warning'
    })
    return false
  }
  return true
}

function check_warning(object, message) {
  if (object === '' || object === undefined || object === null) {
    if (confirm(message + '为空，无论如何也要上传吗？')) {
      return true
    } else {
      return false
    }
  }
  return true
}

function check_error(object, error_message, saved) {
  if (object === '' || object === undefined || object === null) {
    saved.$notify({
      title: '警告',
      message: error_message + '为空， 无法上传！',
      type: 'warning'
    })
    return false
  }
  return true
}

function initpage() {
  window.sessionStorage.removeItem('is_load', 'username', 'is_superuser')
  window.sessionStorage.setItem('is_load', 'username', 'is_superuser')
  window.sessionStorage.is_load = 'false'
  window.sessionStorage.username = ''
  window.sessionStorage.is_superuser = 'false'
}

export {
  get_url,
  checknum,
  checkcount,
  check_warning,
  check_error,
  MAX_VALUE,
  initpage
}
