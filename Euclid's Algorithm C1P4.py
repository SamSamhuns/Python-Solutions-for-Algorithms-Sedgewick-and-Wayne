{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red154\green154\blue154;\red255\green255\blue254;\red0\green0\blue0;
\red144\green1\blue18;\red0\green0\blue255;\red19\green120\blue72;}
{\*\expandedcolortbl;;\cssrgb\c66667\c66667\c66667;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c0\c100000;\cssrgb\c3529\c53333\c35294;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl420\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Chapter 1 Page 4\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Euclid's Algorithm\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl420\partightenfactor0
\cf5 \cb3 \strokec5 '''\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 Compute the greatest common divisor of\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 two nonnegative integers p and q as follows:\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 If q is 0, the answer is p. If not, divide p by q\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 and take the remainder r. The answer is the\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 greatest common divisor of q and r.\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 '''\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl420\partightenfactor0
\cf6 \cb3 \strokec6 def\cf4 \strokec4  gcd( p, q ):\cb1 \
\pard\pardeftab720\sl420\partightenfactor0
\cf4 \cb3   \cf6 \strokec6 if\cf4 \strokec4  q == \cf7 \strokec7 0\cf4 \strokec4  :            \cf2 \strokec2 # Base case\cf4 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 return\cf4 \strokec4  p\cb1 \
\cb3   r = p % q\cb1 \
\cb3   \cf6 \strokec6 return\cf4 \strokec4  gcd(q, r)       \cf2 \strokec2 # Recursive approach    \cf4 \cb1 \strokec4 \
}