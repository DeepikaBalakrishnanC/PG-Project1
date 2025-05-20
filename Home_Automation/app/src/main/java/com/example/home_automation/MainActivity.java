package com.example.home_automation;

import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
EditText ed;
Button bt;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        bt=(Button) findViewById(R.id.button);
        ed=(EditText) findViewById(R.id.editTextTextPersonName);
        bt.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        String ipval=ed.getText().toString();
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        SharedPreferences.Editor ed=sh.edit();
        ed.putString("ip",ipval);
        ed.commit();

        startActivity(new Intent(getApplicationContext(),Login.class));

    }

}