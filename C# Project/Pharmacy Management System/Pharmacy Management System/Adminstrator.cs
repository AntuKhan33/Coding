using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pharmacy_Management_System
{
    public partial class Adminstrator : Form
    {
        String user = "";
        public Adminstrator()
        {
            InitializeComponent();
        }
        public string ID
        {
            get { return user.ToString(); }
        }

        
        public Adminstrator(String username)
        {
            InitializeComponent();
            userNameLabel.Text = username;
            user = username;
            uC_ViewUser1.ID = ID;
            uC_Profile1.ID = ID;
        }

        private void guna2Button1_Click(object sender, EventArgs e)
        {
            uC_Dashboard1.Visible=true;
            uC_Dashboard1.BringToFront();
        }

        private void btnLogout_Click(object sender, EventArgs e)
        {
            Form1 fm = new Form1();
            fm.Show();
            this.Hide();
        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {

        }

        private void uC_Dashboard1_Load(object sender, EventArgs e)
        {

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void Adminstrator_Load(object sender, EventArgs e)
        {
            uC_Dashboard1.Visible = false;
            uC_AddUser1.Visible = false;
            uC_ViewUser1.Visible = false;
            uC_Profile1.Visible = false;
            btnDashbord.PerformClick();

        }

        private void btnAddUser_Click(object sender, EventArgs e)
        {
            uC_AddUser1.Visible = true;
            uC_AddUser1.BringToFront();

        }

        private void uC_AddUser1_Load(object sender, EventArgs e)
        {

        }

        private void btnViewUSer_Click(object sender, EventArgs e)
        {
            uC_ViewUser1.Visible = true;
            uC_ViewUser1.BringToFront();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void btnProfile_Click(object sender, EventArgs e)
        {
            uC_Profile1.Visible = true;
            uC_Profile1.BringToFront();
        }

        private void uC_Profile1_Load(object sender, EventArgs e)
        {

        }
    }
}
