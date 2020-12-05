package com.example.brec;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    Button btn_search, btn_rec;
    public String res="";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn_search = findViewById(R.id.book_search);
        btn_search.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, SubActivity.class);
                startActivity(intent);
            }
        });

        btn_rec = (Button) findViewById(R.id.book_rec);
        btn_rec.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, RecActivity.class);
                startActivity(intent);

                /*
                String url = "http://34.229.136.176:5000/recommend";
                ContentValues val = new ContentValues();
                val.put("name", "cmc");
                val.put("age", "27");
                val.put("잘된다", "굳");
                //AsyncTask를통해 http수행 - arguments주의
                NetworkTask net = new NetworkTask(url, val);
                net.execute();


                Toast toast2 = Toast.makeText(getBaseContext(), res, Toast.LENGTH_SHORT);
                toast2.show();

                 */
            }
        });
    }


}