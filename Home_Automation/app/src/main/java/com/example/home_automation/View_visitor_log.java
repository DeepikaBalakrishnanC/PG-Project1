package com.example.home_automation;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ListView;

public class View_visitor_log extends AppCompatActivity {
ListView lst1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_visitor_log);
        lst1=(ListView) findViewById(R.id.listView1);
    }
}