package com.example.brec;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    Button btn_search, btn_rec;

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
                String greeting = "님 가입을 환영합니다";
                Toast toast = Toast.makeText(getBaseContext(), greeting, Toast.LENGTH_SHORT);
                toast.show();
                //Intent intent = new Intent(MainActivity.this, SubActivity.class);
                //startActivity(intent);
            }
        });
    }
}