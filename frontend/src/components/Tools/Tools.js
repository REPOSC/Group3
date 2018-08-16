function get_url() {
  return 'http://192.168.55.33:8000/'
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

export {
  get_url,
  checknum,
  checkcount,
}
