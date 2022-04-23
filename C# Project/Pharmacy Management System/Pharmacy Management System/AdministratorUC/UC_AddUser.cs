using System;
using System.Windows.Forms;

namespace Pharmacy_Management_System.AdministratorUC
{
    public partial class UC_AddUser : UserControl
    {
        function fn = new function();

        String query;

        public UC_AddUser()
        {
            InitializeComponent();
        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void guna2DateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void guna2TextBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void btnSignUp_Click(object sender, EventArgs e)
        {
            String role = txtUserRole.Text;
            String name = txtName.Text;
            String dob = txtDob.Text;
            Int64 mobile = Int64.Parse(txtMobileNo.Text);
            String email = txtEmail.Text;
            String username = txtUserName.Text;
            String pass = txtPassword.Text;

            try
            {

                query = "insert into users (userRole,name,dob,mobile,email,username,pass) values ('" + role + "','" + name + "','" + dob + "','" + mobile + "','" + email + "','" + username + "','" + pass + "')";
                fn.setData(query, "Signup Successful");
            }
            catch (Exception)
            {
                MessageBox.Show("Username already exist or value error", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

            }
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            clearAll();
        }

        public void clearAll()
        {
            txtName.Clear();
            txtDob.ResetText();
            txtMobileNo.Clear();
            txtEmail.Clear();
            txtUserName.Clear();
            txtPassword.Clear();
            txtUserRole.SelectedIndex = -1;

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void txtName_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtUserName_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
