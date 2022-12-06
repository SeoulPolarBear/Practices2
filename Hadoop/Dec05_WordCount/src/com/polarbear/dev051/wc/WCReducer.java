package com.polarbear.dev051.wc;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

//Hadoop작업 두번째 단계 : Combine
// 는 알아서 처리 됨

//Hadoop작업 세번쨰 단계 : Reduce
// in : sleepy<1,1,1> >> 앞의 두자리에 있는 것들
// out : sleepy 3     >> 뒤에 두자리에 있는 것들



                            //앞의 두자리 Mapper쪽 뒤의 두자리와 같아야 함 (마치 matrix dot 이랑 같다)
public class WCReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

    //메모리 아껴주기 위한 singleton처리 (결과처리)
    private static final IntWritable SUM = new IntWritable();


    //in : sleepy <1,1,1> 한세트 만날때마다 호출할 method
    @Override
    protected void reduce(Text key, //map단계에서 해준 key값 : sleepy
                          Iterable<IntWritable> values, // list비스무리한~ : <1,1,1>
                          Reducer<Text, IntWritable, Text, IntWritable>.Context context) //결과 처리용
            throws IOException, InterruptedException {
        super.reduce(key, values, context);

        int sum = 0;
        //<1,1,1> 합쳐주는 작업
        for(IntWritable i : values){
            //sum은 int, i는 IntWritable => 형 변환을 해줘야...!
            sum += i.get(); // 1 + 1 + 1 = 3
        }
        //Hadoop에서 사용할 수 있게 세팅해주는 단계
        SUM.set(sum);
        context.write(key,SUM);
    }
}
