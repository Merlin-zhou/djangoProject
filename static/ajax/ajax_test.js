// @Time    : 2020/10/20 14:35:56
// @Author  : by ji.zhou


// dns解析
function dns_resolver() {
    // $("#submit").value('傳送中......');
    //清除上次的结果
    $("#result_dns").val('');

    const domain = document.getElementById('domain').value;

    if (domain == '' || domain== undefined || domain == null) {
        document.getElementById('domain').style.border = '1px solid red'   //边框红色提示输入为空
        // document.getElementById('domain').style.color = 'red'
        console.log(11)
        return
        // alert("域名不能为空");
        // domain.value="";
        // domain.focus();
    }
    else {
        document.getElementById('domain').style.border=''
        axios.get('/api/dns', {
            params: {
                domain: domain
            }
        })
            .then(function (response) {
                // handle success
                if (response.data.code === 200){
                    $("#result_dns").val(response.data.ip_list);
                    // $("#result").show();
                }
                else {
                    alert(response.data.msg)
                    // console.log(response);
                    // $("#result").html(response.data);
                    // $("#result").show();
                }
            })
            .catch(function (error) {
                // handle error
                console.log(error);
                // alert(error);
            });
    }
}

// 接口请求
function http_request(){
    $("#result_post").val('');
    const radio = document.getElementsByName('request_method');
    let request_method
    try {
        for (let i=0; i<radio.length; i++) {
            if (radio[i].checked) {
                request_method = radio[i].value;
            }
        }
    }
    catch (error){
        console.log(error);
    }
    const url = document.getElementById('url').value;
    const data = document.getElementById('re_data').value;
    const header = document.getElementById('header').value;
    console.log(url)
    if (url == '' || url== undefined || url == null) {
        console.log(222)
        $("#warning").alert();
    }
    else{
        axios.get('/api/http-post', {
            params: {
                url: url,
                method: request_method,
                header: header,
                data: data,
            }
        })
            .then(function (response) {
                response.data = JSON.stringify(response.data, null,4)     // 将object转json显示在textarea区域, 4缩进
                $("#result_post").val(response.data);
                // $("#result_post").html(response.data);
            })
            .catch(function (error) {
                console.log(error);
            })
    }
}

// 数据库数据插入、查询
function insert_sql(){
    $("#result_sql").val('');
    console.log(111)
    const sql = document.getElementById('make_sql').value;
    console.log(typeof sql)
    const project_name = document.getElementById('sql_select').value;
    console.log(project_name)
    if (project_name =='' || project_name == undefined || project_name == null || project_name == 'database_name'){
        document.getElementById('sql_select').style.border = '1px solid red'   //边框红色提示输入为空
        return
    }
    if (sql == '' || sql== undefined || sql == null) {
        document.getElementById('sql_select').style.border = ''
        document.getElementById('make_sql').style.border = '1px solid red'   //边框红色提示输入为空
        return
    }
    else{
        document.getElementById('make_sql').style.border = ''
        document.getElementById('sql_select').style.border = ''
        axios.get('api/sql_insert', {
            params: {
                sql: sql,
                name: project_name,
            }
        })
            .then(function (response) {
                response.data = JSON.stringify(response.data, null,4)     // 将object转json显示在textarea区域, 4缩进
                $("#result_sql").val(response.data);
                // $("#result_post").html(response.data);
            })
            .catch(function (error) {
                console.log(error);
            })
    }
}

function select_box(){
    axios.get('api/sql_project', {
        params: {
        }
    })
        .then(function (response) {
            const sql_select = document.getElementById('sql_select')
            const list = response.data['project_list']
            // 循环将接口内容赋值给select标签,2个方法
            // 1
            for (let i = 0; i < list.length; i++) {
                const project_name = list[i]['project_name']
                // obj.options.add(new Option("text","value"));这个兼容IE与firefox
                sql_select.options.add(new Option(project_name, project_name))
            }
            // 2
            // const frag = document.createDocumentFragment()
            // for (let i=0;i<list.length;i++){
            //     const option = document.createElement('option')
            //     option.value = list[i]['project_name']
            //     option.innerHTML = list[i]['project_name']
            //     frag.appendChild(option)
            //
            // }
            //  sql_select.appendChild(frag)
        })
        .catch(function (error) {
            console.log(error);
        })
}


/*
对 id 名为 submit 的按钮 onclick 处理函数的绑定工作，另一个是将 id 为 output 的元素隐藏。其实不隐藏也无所谓，因为它本来就是空的，因此你也看不到东西。不过如果有其它的东西这样的处理却也不错。
$() 是 jQuery 提供的一个 getElement() 函数别名，它将根据元素的 id 来得到某个对象。
hide() 是隐藏某个元素。想要显示某个元素可以使用 show() 。
*/

function init() {
    $("#submit_dns").click(function () {
        dns_resolver();
    });
    $("#submit_request").click(function () {
        http_request();
    })
    $("#submit_data").click(function (){
        insert_sql()
    })
    // $(document).ready(function() {
    //     select_box()
    // })

    // $("#output").hide();
}

// 将 init() 函数加到 window.onload 的响应事件对列中。浏览器在装载完一个页面后，会自动调用 onload 事件处理。因此在这里是进行初始化的最好的地方。
$(function(){
    init();
});