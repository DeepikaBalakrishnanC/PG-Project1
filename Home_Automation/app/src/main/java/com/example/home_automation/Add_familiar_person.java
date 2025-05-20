package com.example.home_automation;

import android.media.Image;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;

public class Add_familiar_person extends AppCompatActivity implements View.OnClickListener {
ImageView img;
EditText et1;
EditText et2;
Button bt1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_familiar_person);
        img=(ImageView) findViewById(R.id.imageView);
        et1=(EditText) findViewById(R.id.editTextTextPersonName6);
        et2=(EditText) findViewById(R.id.editTextTextPersonName7);
        bt1=(Button) findViewById(R.id.button3);
        bt1.setOnClickListener(this);

    }

    @Override
    public void onClick(View view) {

    }
}