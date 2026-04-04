; ModuleID = "js_compiler"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 5, i32* %"x"
  %"y" = alloca i32
  store i32 3, i32* %"y"
  %".4" = load i32, i32* %"x"
  %".5" = load i32, i32* %"y"
  %".6" = add i32 %".4", %".5"
  %"sum" = alloca i32
  store i32 %".6", i32* %"sum"
  %".8" = load i32, i32* %"sum"
  %".9" = bitcast [4 x i8]* @"fstr_1" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".8")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr_1" = internal constant [4 x i8] c"%d\0a\00"