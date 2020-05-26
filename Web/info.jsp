<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="myBean.*"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원 정보</title>
</head>
<body>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="userInfo" class="myBean.UserInfo" scope="page"/>
<jsp:setProperty name="userInfo" property="*"/>

<h2>입력하신 회원정보 입니다.</h2>

아이디 : <jsp:getProperty name="userInfo" property="userId"/><br>
비밀번호 : <jsp:getProperty name="userInfo" property="userPass"/><br>
생년월일 : <jsp:getProperty name="userInfo" property="birthday"/><br>

<%
	if(userInfo.getAge() != -1){
%>
나이 : <jsp:getProperty name="userInfo" property="age"/>
<%
	}
%>

</body>
</html>