package com.polarbear.dev051.wc;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.io.Text;
import java.io.IOException;
import java.util.StringTokenizer;

//Hadoop작업의 첫단계 map

//1단계 : 다운받은 소설책을 분석하라고 넣어줄 것!
//      >> Key : 없고, Value : String (hadoop에서는 String이 Text라고 사용이 된다.)
//2단계 : 결과를 받아오기(IntWritable)
//      >> key : String, Value : int
//      ex) I, 1
//          am, 1
//          sleep, 1
public class WCMapper extends Mapper<Object, Text,Text, IntWritable> {
    //결과처리를 위해 자료형을 맞추려면 아예 메소드 밖으로 빼서 자료형을 맞춰야...
    // 메모리 절약하기 위해서 -> singleton처리

    private static final Text WORD = new Text();
    private static final IntWritable ONE = new IntWritable(1);


    //Map을 override >> 한 문장마다 이 method가 호출이 될 것
    @Override
    protected void map(Object key, // Data의 유무 체크(별로 중요하지는 않음)
                       Text value, // ** 중요** 그 문장 자체 << 해당하는 문장을 가져오기 위해 필요한 것
                       Mapper<Object, Text, Text, IntWritable>.Context context) //결과처리용
            throws IOException, InterruptedException {
        //기존에 사용하던 String 객체로 바꿔주는 작업
        String line = value.toString();

        //정확하게 단어의 위치를 체크해아 할 때 : spilt
        //지금 우리가 하려는 것 : 단순히 단어 체크 : StringTokenizer

        StringTokenizer st = new StringTokenizer(line," ");
        
        while(st.hasMoreTokens()){ // 반복문 돌려서
            //결과처리...(자료형을 맞춰줘야한다. (hadoop에서 또 사용을 해야하기 때문에))
            WORD.set(st.nextToken());
            context.write(WORD,ONE);
        }





        super.map(key, value, context);

    }
}
