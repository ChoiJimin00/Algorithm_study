<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" session="false"%>
<%
request.setCharacterEncoding("utf-8");

HttpSession session = request.getSession(true);
String name = request.getParameter("name");
String id = request.getParameter("id");
String pwd = request.getParameter("pwd");

session.setAttribute("login.name",name);
session.setAttribute("login.id",id);
session.setAttribute("login.pwd",pwd);

session.setAttribute("login.time", new Long(System.currentTimeMillis()));
//System.currentTimeMillis()가 리턴하는 long형 정수를 Wrapper Class를 사용하여 Long 객체로 저장
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>HttpSession ...</title>
</head>
<body>

<h3 style="text-align:center">안녕하세요<%=name %>님</h3>
<a href="showinfo.jsp">로그인 정보 보기</a>
</body>
</html>