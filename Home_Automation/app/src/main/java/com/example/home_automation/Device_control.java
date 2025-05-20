package com.example.home_automation;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.Spinner;
import android.widget.TextView;

public class Device_control extends AppCompatActivity implements View.OnClickListener {
TextView txt1;
Spinner sp1;
SeekBar sb;
Button bt3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_device_control);
        txt1=(TextView) findViewById(R.id.textView);
        sp1=(Spinner) findViewById(R.id.spinner);
        sb=(SeekBar) findViewById(R.id.seekBar);
        bt3=(Button) findViewById(R.id.button5);
        bt3.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {

    }
}