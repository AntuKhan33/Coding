using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pharmacy_Management_System.PharmacistUC
{
    public partial class UC_P_UpdateMedicine : UserControl
    {
        function fn = new function();
        String query;
        public UC_P_UpdateMedicine()
        {
            InitializeComponent();
        }

        private void btnSearch_Click(object sender, EventArgs e)
        {
            if (txtMedID.Text != "")
            {
                query = "select * from medic where mid ='" + txtMedID.Text + "'";
                DataSet ds = fn.getData(query);
                if (ds.Tables[0].Rows.Count != 0)
                {
                    txtMediName.Text=ds.Tables[0].Rows[0][2].ToString();
                    txtMediNumber.Text = ds.Tables[0].Rows[0][3].ToString();
                    txtMDate.Text = ds.Tables[0].Rows[0][4].ToString();
                    txtEDate.Text = ds.Tables[0].Rows[0][5].ToString();
                    txtAvailableQuantity.Text = ds.Tables[0].Rows[0][6].ToString();
                    txtPricePerUnit.Text = ds.Tables[0].Rows[0][6].ToString();

                }
                else
                {
                    MessageBox.Show("No Medicine with ID :" + txtMedID.Text + "exist.", "Info", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else
            {
                clearAll();
            }
        }
        private void clearAll()
        {   
            txtMedID.Clear();
            txtMediName.Clear();
            txtMediNumber.Clear();
            txtMDate.ResetText();
            txtEDate.ResetText();
            txtAvailableQuantity.Clear();
            txtPricePerUnit.Clear();
            if(txtAddQuan.Text != "0")
            {
                txtAddQuan.Text = "0";
            }
            else
            {
                txtAddQuan.Text = "0";
            }
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            clearAll();
        }

        Int64 totalquantity;
        //private void btnadd_click(object sender, eventargs e)
        //{
        //    string mname = txtmediname.text;
        //    string mnumber =txtmedinumber.text;
        //    string mdate = txtmdate.text;
        //    string edate = txtedate.text;
        //    int64 quantity = int64.parse(txtavailablequantity.text);
        //    int64 addquantity = int64.parse(txtaddquan.text);
        //    int64 unitprice = int64.parse(txtpriceperunit.text);
        //    totalquantity = quantity + addquantity;


        //    query = "update medic set mname ='" + mname + "',mnumber='" + mnumber + "',mdate='" + mdate + "',edate='" + edate + "',quantity='" + totalquantity + "',perunit='" + unitprice + "'where mid ='" + txtmedid.text + "' ";
        //    fn.setdata(query, "medicine details successfull");

        //}



       


        private void txtMedID_TextChanged(object sender, EventArgs e)
        {

        }

        private void UC_P_UpdateMedicine_Load(object sender, EventArgs e)
        {

        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {
            String mname = txtMediName.Text;
            String mnumber = txtMediNumber.Text;
            String mdate = txtMDate.Text;
            String edate = txtEDate.Text;
            Int64 quantity = Int64.Parse(txtAvailableQuantity.Text);
            Int64 addquantity = Int64.Parse(txtAddQuan.Text);
            Int64 unitprice = Int64.Parse(txtPricePerUnit.Text);
            totalquantity = quantity + addquantity;


            query = "update medic set mname ='" + mname + "',mnumber='" + mnumber + "',mDate='" + mdate + "',eDate='" + edate + "',quantity='" + totalquantity + "',perUnit='" + unitprice + "'where mid ='" + txtMedID.Text + "' ";
            fn.setData(query, "Medicine Details Successfull");
        }
    }
}
