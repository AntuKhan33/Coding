using System;
using System.Windows.Forms;

namespace Calculator
{
	public partial class Form1 : Form
	{
		public Form1() => InitializeComponent();

		private string Action { get; set; } = "";

		private double FirstNumber { get; set; } = 0;

		private double SecondNumber { get; set; } = 0;

		private double Result { get; set; } = 0;

		private void button1_Click(object sender, EventArgs e) => AddTextToLabel(button1);
		private void button2_Click(object sender, EventArgs e) => AddTextToLabel(button2);
		private void button3_Click(object sender, EventArgs e) => AddTextToLabel(button3);
		private void button4_Click(object sender, EventArgs e) => AddTextToLabel(button4);
		private void button5_Click(object sender, EventArgs e) => AddTextToLabel(button5);
		private void button6_Click(object sender, EventArgs e) => AddTextToLabel(button6);
		private void button7_Click(object sender, EventArgs e) => AddTextToLabel(button7);
		private void button8_Click(object sender, EventArgs e) => AddTextToLabel(button8);
		private void button9_Click(object sender, EventArgs e) => AddTextToLabel(button9);
		private void button10_Click(object sender, EventArgs e) => AddTextToLabel(button10);
		private void button15_Click(object sender, EventArgs e) => AddTextToLabel(button15);

		private void AddTextToLabel(Button button) => label1.Text += button.Text;

		private void button11_Click(object sender, EventArgs e)
		{
			FirstNumber = Convert.ToDouble(label1.Text);
			label1.Text = "";
			Action = "+";
		}

		private void button12_Click(object sender, EventArgs e)
		{
			FirstNumber = Convert.ToDouble(label1.Text);
			label1.Text = "";
			Action = "-";
		}
		private void button16_Click(object sender, EventArgs e)
		{ 
			FirstNumber = Convert.ToDouble(label1.Text);
			label1.Text = "";
			Action = "*";

		}
		private void button17_Click(object sender, EventArgs e)
		{
			FirstNumber = Convert.ToDouble(label1.Text);
			label1.Text = "";
			Action = "/";

		}
		private void button13_Click(object sender, EventArgs e)
		{
			SecondNumber = Convert.ToDouble(label1.Text);
			if (Action == "+")
			{
				Result = FirstNumber + SecondNumber;
				label1.Text = Result.ToString();
			}
			if (Action == "-")
			{
				Result = FirstNumber - SecondNumber;
				label1.Text = Result.ToString();
			}
			if (Action == "*")
			{
				Result = FirstNumber * SecondNumber;
				label1.Text = Result.ToString();
			}
			if (Action == "/")
			{
				Result = FirstNumber / SecondNumber;
				label1.Text = Result.ToString();
			}


		}

		private void button14_Click(object sender, EventArgs e)
		{
			label1.Text = "";
			FirstNumber = 0;
			SecondNumber = 0;
		}

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
