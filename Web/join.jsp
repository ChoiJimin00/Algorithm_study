<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원가입</title>
<style>
td.title{text-algin:right}
td.bottom{text-align:center}
</style>
<script>
function fnCheck(){
	var userId = document.getElementById("userId");
	var userPass = document.getElementById("userPass");
	var userPassConfirm = document.getElementById("userPassConfirm");
	var birthday = document.getElementById("birthday");
	
	if(userId.value==""){
		alert("아이디를 입력하세요.");
		userId.focus();
		return false;
	} else if(userPass.value==""){
		alert("비밀번호를 입력하세요.");
		userPass.focus();
		return false;
	} else if(userPassConfirm.value==""){
		alert("비밀번호를 입력하세요.");
		userPassConfirm.focus();
		return false;
	} else if(userPass.value != userPassConfirm.value){
		alert("비밀번호가 일치하지 않습니다.");
		userPass.value="";
		userPassConfirm.value="";
		userPass.focus();
		return false;
	} else if(birthday.value==""){
		alert("생년월일을 입력하세요.(20000101)");
		birthday.focus();
		return false;
	}
	return true;
}
</script>
</head>
<body>
<h2>회원 가입</h2>
<form action="info.jsp" method="post" onSubmit="return fnCheck()">
<table border="1" style="border-collapse:collapse">
<tr><td class="title">아이디</td>
<td><input type="text" id="userId" name="userId"></td></tr>
<tr><td class="title">비밀번호</td>
<td><input type="password" id="userPass" name="userPass"></td></tr>
<tr><td class="title">비밀번호확인</td>
<td><input type="password" id="userPassConfirm" name="userPassConfirm"></td></tr>
<tr><td class="title">생일월일 </td>
<td><input type="text" id="birthday" name="birthday"></td></tr>
<tr><td class="bottom" colspan="2">
<input type="submit" value="join">
<input type="reset" value="reset"></td></tr>
</table>
</form>
</body>
</html>