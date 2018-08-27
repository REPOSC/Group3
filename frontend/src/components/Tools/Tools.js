const MAX_VALUE = 12

function get_url() {
  return 'http://139.199.106.168:8000/'
}

function checkcount(number) {
  if (!checknum(number)) {
    return false
  }
  if (parseInt(number) > 10000) {
    alert('输入的数字过大，请检查')
    return false
  } else if (parseInt(number) === 0) {
    alert('个数不能为0！')
    return false
  }
  return true
}

function checknum(number) {
  for (let i = 0; i < number.length; ++i) {
    if (number[i] > '9' || number[i] < '0') {
      alert('输入的数字非法，请检查')
      return false
    }
  }
  if (number.length === 0) {
    alert('输入的数字非法，请检查')
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

function check_error(object, message) {
  if (object === '' || object === undefined || object === null) {
    alert(message + '为空， 无法上传！ ')
    return false
  }
  return true
}

function del_element(array, arr_element) {
  let index = -1
  for (let i = 0; i < array.length; ++i) {
    if (array[i] === arr_element) {
      index = 1
      break
    }
  }
  if (index === -1) {} else {
    array.splice(index, 1)
  }
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
  del_element,
  check_warning,
  check_error,
  MAX_VALUE,
  initpage
}
