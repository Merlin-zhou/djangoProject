// @Time    : 2020/11/5 17:33:32
// @Author  : ji.zhou

new Vue ({
    el:'#app',
    data: function () {
        return{
            input: '',
            userInfo: {     //添加用户信息
                name: '',
                gender: '',
                tel: '',
                birthday: '',
            },
            tableData: [{
                birthday: '2016-05-02',
                name: '王小虎',
                tel: '18819876543',
                gender: '男'
            }]
        }
    },
    methods: {
        //添加
        addUser() {
            if (!this.userInfo.name) {
                this.$message({
                    message: '请输入姓名',
                    type: 'warning'
                });
                return
            }
            if (!this.userInfo.gender) {
                this.$message({
                    message: '请输入性别',
                    type: 'warning'
                });
                return
            }
            if (!/^1[3456789]\d{9}$/.test(this.userInfo.tel)) { //正则判断电话号码
                this.$message({
                    message: '电话号码格式有误',
                    type: 'warning'
                });
                return
            }
            if (!this.userInfo.birthday) {
                this.$message({
                    message: '请输入出生日期',
                    type: 'warning'
                });
                return
            }
            this.tableData.push(this.userInfo);
            this.userInfo = {
                name: '',
                gender: '',
                tel: '',
                birthday: '',
            };
        },
        // 删除数据
        delUser(idx, row) {
            console.log(idx, row);
            // this.tableData.splice(idx, 1);
        },
    }
})