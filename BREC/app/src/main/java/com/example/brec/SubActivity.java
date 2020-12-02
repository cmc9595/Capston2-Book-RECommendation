package com.example.brec;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentTransaction;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class SubActivity extends AppCompatActivity {

    private Button searchBtn;
    private String keyword;

    /*@Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sub);

        searchBtn = findViewById(R.id.searchBtn);

        searchBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                TextView searchText = (TextView) findViewById(R.id.searchText);
                //final TextView searchResult = (TextView) findViewById(R.id.searchResult);
                keyword = searchText.getText().toString();

                Intent intent = new Intent(SubActivity.this, SubActivity.class);
                intent.putExtra("keyword", keyword);
                startActivity(intent);
                //searchResult.setText(str);


            }
        });
    }*/
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sub);
        SearchFragment searchFragment = new SearchFragment();
        FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
        transaction.add(R.id.frame_layout_contents, searchFragment);
        transaction.commit();
    }
}