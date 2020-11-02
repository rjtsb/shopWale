function validate(){  
var x=document.loginform.email.value; 
var at=x.indexOf("@");  
var dot=x.lastIndexOf(".");  
if (at<1 || dot<at+2 || dot+2>=x.length){  
  alert("Please enter a valid e-mail address...");  
  return false;
}
}

function validateSignup(){  
	var email=document.signupform.email.value;  
	var password=document.signupform.password.value;
	var name = document.signupform.name.value;
	var mobile = document.signupform.mobile.value;
	var pin = document.signupform.pin.value;
	var at=email.indexOf("@");  
	var dot=email.lastIndexOf(".");

	if (name==null || name==""){  
	  alert("Name can't be blank");  
	  return false;}
	else if (email==null || email==""){  
	  alert("Email can't be blank");  
	  return false;}
	else if (mobile==null || mobile==""){  
	  alert("Mobile number can't be blank");  
	  return false; }
	else if (password==null || password==""){  
	  alert("Password can't be blank");  
	  return false;}
	else if (isNaN(pin) || isNaN(mobile)){  
	  alert("Enter Numeric value only for Mobile and Pin ");  
	  return false;}
	else if (at<1 || dot<at+2 || dot+2>=email.length){  
	  alert("Please enter a valid e-mail address...");  
	  return false;}
	else if(password.length<6){  
	  alert("Password must be at least 6 characters long.");  
	  return false;  
	  }
	 else if(mobile.length!=10){  
	  alert("Mobile number must be 10 characters long.");  
	  return false;  
	  }
	else{
		return true;
	}
}  