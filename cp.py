<?php
error_reporting(0);
session_start();
//color
$res="\033[0m";
$red="\033[0;31m";
$green="\033[0;32m";
$yellow="\033[0;33m";
$white= "\033[0;37m";  
$red = "\e[0;31m";
$blu = "\e[0;34m";
$gre = "\e[0;32m";
$bgr = "\e[1;32m";
$bre = "\e[1;31m";
$bye = "\e[1;33m";
$bcy = "\e[1;36m";
$res = "\e[0m";
$xtab = mt_rand();
$today = date("dmY");
$res="\033[0m";
$red="\033[0;31m";
$green="\033[0;32m";
$yellow="\033[0;33m";
$white= "\033[0;37m";
$purple="\033[0;35m";
$blue="\033[0;34m";
$cyan="\033[0;36m";
//keylock
   $checkkey = file('https://hangbz.000webhostapp.com/key.php');
    $lock = file_get_contents('https://hangbz.000webhostapp.com/lock.php');
    $keylock = md5(htmlspecialchars($lock));
    echo $res;
    if (md5('HanGudboiz') != $keylock) {
        exit($red . "Server Đã Ngừng Hoạt Động !!!
$res");
    } else {
        echo $bcy. "Server Hoạt Động$res";
        sleep(1);
    }
    echo "
";
    while (true) {
        echo "[1;36mNhập Api Key: [1;33m";
        $makey = trim(fgets(STDIN));
        if ($makey == $checkkey[0]) {
            echo "[1;32mkey chính xác...";
            echo "
";
            break;
        } else {
            echo "[1;31mMã key Không Đúng Kìa... \n";
            sleep(1);
            echo "Vui Lòng Donate Cho Mình Để Có Key\n";
            sleep(1);
            echo $bcy."Donate qua Momo:0392279447 or Donate qua Xu_Tds:HanGudboizTools  \n";
            echo"
";
        }
    }
    @system('clear');
//config
{echo $green."\033[1;32mĐang Vào Tool Nè Má Ơi:'< \n$ress";
sleep(3);
@system('clear');
$listnv = [];
echo $white."\n\n";
                   echo"\033[0;32m
=============================================

       __  _____    _   __   __________
      / / / /   |  / | / /  / ____/ __ )____
     / /_/ / /| | /  |/ /  / / __/ __  /_  /
    / __  / ___ |/ /|  /  / /_/ / /_/ / / /_
   /_/ /_/_/  |_/_/ |_/   \____/_____/ /___/

 =============================================\n\n";
sleep(1.5);                             
echo $bcy."🌸🌸🌸Đưa cho anh hương ngát thơm nơi đây
Và đưa con tim anh lãng du theo mây
Khi mưa đang rơi áng mây che trời
Em như tia nắng sớm mai bên đời...\n\n\n";
sleep(2);
echo "\033[1;32m=>>>Tặng Xu Donate cho mình lấy động lực viết tools nhé💕\n\n";
sleep(2);
echo $bcy."🌸Đang tiến hành chạy tool...\n";

sleep(2);
echo $blue.="\033[0;34mHãy Nhập Tài Khoản TDS: $yellow\033[1;32m";
$_SESSION["username"]=trim(fgets(STDIN));
echo $green."\033[1;33mHãy Nhập Mật Khẩu TDS: $yellow\033[1;32m";
$_SESSION['password']=trim(fgets(STDIN));
echo $bre."\e[1;31mHãy Nhập Cookie Facebook: $yellow\033[1;32m";
$cookie=trim(fgets(STDIN));
echo"$res\n";
$ch=curl_init();
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_URL, 'https://traodoisub.com/scr/login.php');
curl_setopt($ch, CURLOPT_COOKIEJAR, "TDS.txt");
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935K/KKU3ETG2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36');
$login =array('username' => $_SESSION['username'],'password' => $_SESSION['password'],'submit' => ' Đăng Nhập');
curl_setopt($ch, CURLOPT_POST,count($login));
curl_setopt($ch, CURLOPT_POSTFIELDS,$login);
curl_setopt($ch, CURLOPT_COOKIEFILE, "TDS.txt");
$source=curl_exec($ch);
curl_close($ch);
$tk = $_SESSION["username"];
$mk = $_SESSION['password'];
#get_token
$ch=curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed');
$head[] = "Connection: keep-alive";
$head[] = "Keep-Alive: 300";
$head[] = "authority: m.facebook.com";
$head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
$head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
$head[] = "cache-control: max-age=0";
$head[] = "upgrade-insecure-requests: 1";
$head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
$head[] = "sec-fetch-site: none";
$head[] = "sec-fetch-mode: navigate";
$head[] = "sec-fetch-user: ?1";
$head[] = "sec-fetch-dest: document";
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935K/KKU3ETG2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36');
curl_setopt($ch, CURLOPT_ENCODING, '');
curl_setopt($ch, CURLOPT_COOKIE, $cookie);
curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
curl_setopt($ch, CURLOPT_TIMEOUT, 60);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
$access = curl_exec($ch);
curl_close($ch);
if (explode('\",\"useLocalFilePreview',explode('accessToken\":\"', $access)[1])[0]){
$access_token = explode('\",\"useLocalFilePreview',explode('accessToken\":\"', $access)[1])[0];
if(json_decode(file_get_contents('https://graph.facebook.com/me/?access_token='.$access_token))->{'id'}){
	$idfb = json_decode(file_get_contents('https://graph.facebook.com/me/?access_token='.$access_token))->{'id'};	
}else{
	exit($red."COOKIE Yếu Sinh Lý!");
}
@system('clear');
                   echo"\033[0;32m
=============================================

       __  _____    _   __   __________
      / / / /   |  / | / /  / ____/ __ )____
     / /_/ / /| | /  |/ /  / / __/ __  /_  /
    / __  / ___ |/ /|  /  / /_/ / /_/ / / /_
   /_/ /_/_/  |_/_/ |_/   \____/_____/ /___/

 =============================================\n";
echo"\033[1;36m       \033[1;41m•Tool TDS Của Nguyễn Đình Hân✔\n";
if ($source != 1 && $source != ''){
	echo $white."\033[1;37m================================================================\n\n";
	echo $green."\033[1;31m[\033[1;32m✓\033[1;31m] \033[1;32mChọn nhiệm vụ  \n\n";
	$user = $_SESSION["username"];
	echo $white."\033[1;31m[\033[1;32m✓\033[1;31m] \033[1;32mNhiệm vụ like (y/n): $green\033[1;33m";
	if (trim(fgets(STDIN)) == 'y'){
		array_push($listnv,'like');
		echo $white."\033[1;31m[\033[1;32m✓\033[1;31m] \033[1;32mDelay like : $green\033[1;33m";
		$_SESSION['delaylike']=trim(fgets(STDIN));
		if($_SESSION['delaylike'] < 0)
		{exit($red."[1;31mTối Thiểu Giây\n");}
	}
	echo $white."\033[1;31m[\033[1;32m✓\033[1;31m] \033[1;32mNhiệm vụ sub (y/n): $green\033[1;33m"; 
	if (trim(fgets(STDIN)) == 'y'){
		array_push($listnv,'sub');
		echo $white."\033[1;31m[\033[1;32m✓\033[1;31m] \033[1;32mDelay sub : $green\033[1;33m";
		$_SESSION['delaysub']=trim(fgets(STDIN));
		if($_SESSION['delaysub'] < 0)
		{exit($red."[1;31mTối Thiểu Giây\n");}
	}
	echo $white."\033[1;31m[\033[1;32m✓\033[1;31m] \033[1;32mNhiệm vụ page (y/n): $green\033[1;33m";
	if (trim(fgets(STDIN)) == 'y'){
		array_push($listnv,'page');
		echo $white."\033[1;31m[\033[1;32m✓\033[1;31m] \033[1;32mDelay page : $green\033[1;33m";
		$_SESSION['delaypage']=trim(fgets(STDIN));
		if($_SESSION['delaypage'] < 0)
		{exit($red."[1;31mTối Thiểu Giây\n");}
	}
	
	if (count($listnv) == 0){exit($red."\033[1;31mPhải chọn ít nhất 1 nhiệm vụ");}
	
	echo $white."\033[1;31m[\033[1;32m✓\033[1;31m] \033[1;32mThời gian nghỉ tránh bị block : $green\033[1;33m";
	$_SESSION['j']=trim(fgets(STDIN));
	if($_SESSION['j'] < 0)
	{exit($red."\033[1;31mtối thiểu 1 giây trở lên\n\n");}
	echo $white."\033[1;31m[\033[1;32m✓\033[1;31m] \033[1;32mSố job chạy : $green\033[1;33m";
	$_SESSION['i']=trim(fgets(STDIN));
	if($_SESSION['i'] < 1)
	{exit($red."Tối Thiểu 1 Lần\n\n");}
}else{
	exit($red."\033[1;31mĐăng nhập thất bại");
}
@system('clear');
echo"$lon\n";
         echo"\033[0;32m
     __  __               ______          ____          _    
    / / / /___ _____     / ____/_  ______/ / /_  ____  (_)___
   / /_/ / __ `/ __ \   / / __/ / / / __  / __ \/ __ \/ /_  /
  / __  / /_/ / / / /  / /_/ / /_/ / /_/ / /_/ / /_/ / / / /_
 /_/ /_/\__,_/_/ /_/   \____/\__,_/\__,_/_.___/\____/_/ /___/\n";
    echo"\033[1;36m   \033[1;41m•Bản Quyền Của Nguyễn Đình Hân \n";
echo $white."\033[1;37m============================================================\n\n";;
sleep(1);
echo "\033[1;37m~\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;37m => \033[1;32mFacebook :\033[1;32m Nguyễn Đình Hân \n";
sleep(1);
echo "\033[1;37m~\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;37m => \033[1;32mTặng Xu Donate cho mình lấy động lực viết tools nhé!!!\n";
sleep(1);
echo "\033[1;37m~\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;37m => \033[1;32mUSERNAME DONATE TDS : \033[1;35mHanGudboizTools\n";
sleep(1);
echo "\033[1;37m~\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;37m => \033[1;32mZalo liên hệ :\033[1;32m 0392279447\n";
sleep(1);
echo "\033[1;37m~\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;37m => \033[1;32mTên Tài Khoản : \033[1;35m$user\n";
sleep(1);
echo "\033[1;37m~\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;37m => \033[1;32mĐang Tool Cho ID : \033[1;35m$idfb\n";
$xu = file_get_contents('https://traodoisub.com/scr/test3.php?user='.$user);
sleep(1);
echo $white."\033[1;37m~\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;37m => \033[1;32mỐng Heo Hiện Tại Của Bạn Có : \033[1;32m".$xu." XU \n";
sleep(1);
echo"\033[0;36m          ╭───────────────────────────────────╮
            [🌟]● My Name's : Hân Gudboiz✅
            [🌟]● Zalo      :  0392279447
            [🌟]● Facebook  : Nguyễn Đình Hân\n";
echo"\033[0;32m               ‹—•—•—•—•—•—🌷—•—•—•—•—•—›\n";
echo"\033[0;34m            [⚡]● Tool: Trao Đổi Sub°
            [🌟]● Trạng Thái: Hoạt Động.
          ╰───────────────────────────────────╯\n";
sleep(1);
echo $white."\033[1;37m==============================================================\n\n";
sleep(2);
echo $white."\033[1;37m        TIẾN HÀNH BẮT ĐẦU CHẠY TOOL BY HÂNGUDBOIZ !!\n\n";
$h = datnick($user,$idfb);
if ($h == '1'){
		$i=1;
		while ($i <= $_SESSION['i']){
			$rand = $listnv[array_rand($listnv,1)];
			if ($rand == 'like'){
				$list = getnv('like',$user);
				foreach ($list  as $id) {
					$g = like($access_token,$id,$cookie);
					if ($g->{'error'}->{'code'} == 368){
						exit($red."\033[1;31mĐã bị block \n");
					}
					date_default_timezone_set('Asia/Ho_Chi_Minh');
$ti = date('H:i:s');
$today = date("dmY");
					$s = nhantien('like',$id);
					if ($s == 2){$stt=$stt+1;$xu = $xu + 200;echo "\033[1;37m~\033[1;31m[\033[1;33m$stt\033[1;31m]⚡\033[1;31m[\033[1;33m$ti\033[1;31m]$white$green \033[1;31m[\033[1;32mLIKE\033[1;31m] \033[1;37m=> $green\033[1;33m".$id." 	$bcy
=>Bạn Đã Bỏ Vào Ống Heo 200 Xu $whit \033[1;31m| $green\033[1;32m".$xu." \033[1;32mXU \033[1;31m|" ;}
					else{echo $red."\033[1;37m~\033[1;31m[\033[1;33m$stt\033[1;31m⚡\033[1;31m[\033[1;33m$ti\033[1;31m]$white \033[1;31m:\033[1;31mTiền Nhiều Quá Bỏ Không Vừa Kìa ^.^".$green;}
					echo "\n";
					sleep($_SESSION['delaylike']);
					}
			}else if($rand == 'sub'){
				$list = getnv('follow',$user);
				foreach ($list  as $id) {
					$g = follow($access_token,$id,$cookie);
					if ($g->{'error'}->{'code'} == 368){
						exit($red."\033[1;31mĐã bị block \n");
					}
					$s = nhantien('sub',$id);
					date_default_timezone_set('Asia/Ho_Chi_Minh');
$ti = date('H:i:s');
					if ($s == 2){$stt=$stt+1;$xu = $xu + 600;echo "\033[1;37m~\033[1;31m[\033[1;33m$stt\033[1;31m]⚡\033[1;31m[\033[1;33m$ti\033[1;31m]$white$green \033[1;31m[\033[1;32mFOLLOW\033[1;31m] \033[1;37m=> $green\033[1;33m".$id."$bcy
=>Bạn Đã Bỏ Vào Ống Heo 600 Xu $whit \033[1;31m| $green\033[1;32m".$xu." \033[1;32mXU \033[1;31m|" ;}
					else{echo $red."\033[1;37m~\033[1;31m[\033[1;33m$stt\033[1;31m]⚡\033[1;31m[\033[1;33m$ti\033[1;31m]$white \033[1;31m:\033[1;31mTiền Nhiều Quá Bỏ Không Vừa Kìa ^.^".$green;}
					echo "\n";
					sleep($_SESSION['delaysub']);
				}
			}else if($rand == 'page'){
				$list = getnv('likepage',$user);
				foreach ($list  as $id) {
					page($id,$cookie);
					$s = nhantien('page',$id);
					date_default_timezone_set('Asia/Ho_Chi_Minh');
$ti = date('H:i:s');
					if ($s == 2){$stt=$stt+1;$xu = $xu + 600; echo "\033[1;37m~\033[1;31m[\033[1;33m$stt\033[1;31m]⚡\033[1;31m[\033[1;33m$ti\033[1;31m]$white$green \033[1;31m[\033[1;32mPAGE\033[1;31m] \033[1;37m=> $green\033[1;33m".$id."$bcy
=>Bạn Đã Bỏ Vào Ống Heo 600 Xu $whit \033[1;31m| $green\033[1;32m".$xu." \033[1;32mXU \033[1;31m|" ;}
					else{echo $red."\033[1;37m~\033[1;31m[\033[1;33m$stt\033[1;31m]⚡\033[1;31m[\033[1;33m$ti\033[1;31m]$white \033[1;31mTiền Nhiều Quá Bỏ Không Vừa Kìa ^.^".$green;}
					echo "\n";
					sleep($_SESSION['delaypage']);
				}
			}
		echo $red."\033[1;36mNghỉ ".$_SESSION['j']." \033[1;36mgiây:";
		for ($x = 0; $x <= $_SESSION['j']; $x++) {
		  echo $green."\033[1;36m•";
		  sleep(1);
		}
		echo "\n";
		}
}else{exit($red."\033[1;31mCấu hình thất bại, vui lòng thêm id::\033[1;31m".$idfb." vào cấu hình");}
}else{exit($red."\033[1;31mCookie die!!");}
}
function follow($access_token,$id,$cookie){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://graph.facebook.com/'.$id.'/subscribers');
	$head[] = "Connection: keep-alive";
	$head[] = "Keep-Alive: 300";
	$head[] = "authority: m.facebook.com";
	$head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
	$head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
	$head[] = "cache-control: max-age=0";
	$head[] = "upgrade-insecure-requests: 1";
	$head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
	$head[] = "sec-fetch-site: none";
	$head[] = "sec-fetch-mode: navigate";
	$head[] = "sec-fetch-user: ?1";
	$head[] = "sec-fetch-dest: document";
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935K/KKU3ETG2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
	$data = array('access_token' => $access_token);
	curl_setopt($ch, CURLOPT_POST,count($data));
	curl_setopt($ch, CURLOPT_POSTFIELDS,$data);
	$access = curl_exec($ch);
	curl_close($ch);
	return json_decode($access);
}
function like($access_token,$id,$cookie){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://graph.facebook.com/'.$id.'/likes');
	$head[] = "Connection: keep-alive";
	$head[] = "Keep-Alive: 300";
	$head[] = "authority: m.facebook.com";
	$head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
	$head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
	$head[] = "cache-control: max-age=0";
	$head[] = "upgrade-insecure-requests: 1";
	$head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
	$head[] = "sec-fetch-site: none";
	$head[] = "sec-fetch-mode: navigate";
	$head[] = "sec-fetch-user: ?1";
	$head[] = "sec-fetch-dest: document";
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935K/KKU3ETG2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
	$data = array('access_token' => $access_token);
	curl_setopt($ch, CURLOPT_POST,count($data));
	curl_setopt($ch, CURLOPT_POSTFIELDS,$data);
	$access = curl_exec($ch);
	curl_close($ch);
	return json_decode($access);
}
function cmt($access_token,$id,$cookie,$msg){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://graph.facebook.com/'.$id.'/comments');
	$head[] = "Connection: keep-alive";
	$head[] = "Keep-Alive: 300";
	$head[] = "authority: m.facebook.com";
	$head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
	$head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
	$head[] = "cache-control: max-age=0";
	$head[] = "upgrade-insecure-requests: 1";
	$head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
	$head[] = "sec-fetch-site: none";
	$head[] = "sec-fetch-mode: navigate";
	$head[] = "sec-fetch-user: ?1";
	$head[] = "sec-fetch-dest: document";
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935K/KKU3ETG2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
	$data = array('message' => $msg,'access_token' => $access_token);
	curl_setopt($ch, CURLOPT_POST,count($data));
	curl_setopt($ch, CURLOPT_POSTFIELDS,$data);
	$access = curl_exec($ch);
	curl_close($ch);
	return json_decode($access);
}
function page($id,$cookie){
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://mbasic.facebook.com/'.$id);
	$head[] = "Connection: keep-alive";
	$head[] = "Keep-Alive: 300";
	$head[] = "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
	$head[] = "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935K/KKU3ETG2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect
	:'));
	$page = curl_exec($ch);
	if (explode('&amp;refid=',explode('pageSuggestionsOnLiking=1&amp;gfid=',$page)[1])[0]){
		$get = explode('&amp;refid=',explode('pageSuggestionsOnLiking=1&amp;gfid=',$page)[1])[0];
		$link = 'https://mbasic.facebook.com/a/profile.php?fan&id='.$id.'&origin=page_profile&pageSuggestionsOnLiking=1&gfid='.$get.'&refid=17';
		curl_setopt($ch, CURLOPT_URL, $link);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_exec($ch);
	}	
	curl_close($ch);
}
function camxuc($id,$type,$cookie){
	$ch = curl_init();
	if(strpos($id,'_')){
		$uid = explode('_',$id, 2);
		$id2 = 'story.php?story_fbid='.$uid[1].'&id='.$uid[0];
	}else{
		$id2 = $id;
	}
	curl_setopt($ch, CURLOPT_URL, 'https://mbasic.facebook.com/'.$id2);
	$head[] = "Connection: keep-alive";
	$head[] = "Keep-Alive: 300";
	$head[] = "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
	$head[] = "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G935K/KKU3ETG2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect
	:'));
	$page = curl_exec($ch);
	if ($id2 != $id && explode('&amp;origin_uri=',explode('amp;ft_id=',$page,2)[1],2)[0]){
		$get = explode('&amp;origin_uri=',explode('amp;ft_id=',$page,2)[1],2)[0];
	}else{
		$get = $id2;
	}
	$link = 'https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id='.$get;
	curl_setopt($ch, CURLOPT_URL, $link);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$cx = curl_exec($ch);
	$haha = explode('<a href="',$cx);
	if ($type == 'LOVE'){
		$haha2 = explode('" style="display:block"',$haha[2])[0];
	}else if ($type == 'WOW'){
		$haha2 = explode('" style="display:block"',$haha[5])[0];
	}else if ($type == 'HAHA'){
		$haha2 = explode('" style="display:block"',$haha[4])[0];
	}else if ($type == 'SAD'){
		$haha2 = explode('" style="display:block"',$haha[6])[0];
	}else{
		$haha2 = explode('" style="display:block"',$haha[7])[0];
	}
	$link2 = html_entity_decode($haha2);	
	curl_setopt($ch, CURLOPT_URL, 'https://mbasic.facebook.com'.$link2);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_exec($ch);
	curl_close($ch);
}
function getnv($loai,$user){
	$list = file_get_contents('https://traodoisub.com/scr/api_job.php?chucnang='.$loai.'&user='.$user);
	return json_decode($list);
}
function datnick($user,$id){
	$xxx = file_get_contents('https://traodoisub.com/scr/api_dat.php?user='.$user.'&idfb='.$id);
	return $xxx;
}
function nhantien($loai,$id){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://traodoisub.com/scr/nhantien'.$loai.'.php');
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$tdsxu=array('id' => $id);
	curl_setopt($ch, CURLOPT_POST,count($tdsxu));
	curl_setopt($ch, CURLOPT_POSTFIELDS,$tdsxu);
	curl_setopt($ch, CURLOPT_COOKIEFILE, "TDS.txt");
	$xu=curl_exec($ch);
	curl_close($ch);
	return $xu;
}
function nhantiencx($loai,$id){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://traodoisub.com/scr/nhantiencx.php');
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$tdsxu=array('id' => $id, 'loaicx' => $loai);
	curl_setopt($ch, CURLOPT_POST,count($tdsxu));
	curl_setopt($ch, CURLOPT_POSTFIELDS,$tdsxu);
	curl_setopt($ch, CURLOPT_COOKIEFILE, "TDS.txt");
	$xu=curl_exec($ch);
	curl_close($ch);
	return $xu;
}

