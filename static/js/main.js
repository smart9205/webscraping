
function searchfn()
{
    var select = document.getElementById('selectId');
    console.log(select.value)

    var searchvalue = document.getElementById('search-input')
    console.log(searchvalue.value)

    const name = searchvalue.value;
    const topD = select.value;

    const dict_values = {name, topD} // Pass the javascript variables to a dictionary
    const s = JSON.stringify(dict_values) // Converts a Javascript object or value to a JSON string
    console.log(s);

    

    $.ajax({
        url:"/search",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)
    }).then(res =>{
        let cnt=0
        $(".select-window").empty();

        for(let i=0;i<res.length;i++){
            const em=res[i]      


            
            const img_url = em["url"]
            // const video_url = em["video_url"]
            

            const avtar_img=em["avatar"]
            const duration=em["duration"]
            const views=em["views"]
            const tm = em["tm"]
            
            const title = em["title"]
            const name = em["name"]
            const desc = em["desc"]

            console.log(img_url)


            cnt++;

            $( ".select-window" ).append(              
              `<div class="im-1">
                <div class="im-2" style="background-image: url(${img_url});">  
                    <div class="im-3"> 
                     <p class="font"> ${duration} </p>
                    </div>
                    <div class="im-4">    
                     <p class="font"> ${views} </p>
                    </div>
                    <div class="im-5">   
                      <p class="font">${tm}</p>
                    </div>
                </div>
                <div class="im-6">
                    <div class="im-7">
                        <img src=${avtar_img} style="height:100%; width:100%; object-fit:contain;">    
                    </div> 
                    <div class="im-8">       
                        <div class="im-9">
                          <p class="font2" style="opacity:1; font: size 0.7vw;"> ${title} </p>
                        </div>
                        <div class="im-9">
                          <p class="font2">${name}</p>
                        </div>
                        <div class="im-9">
                          <p class="font2">${desc}</p>
                        </div>
                    </div>
                </div>              
              </div>`
            );
        }
        console.log(cnt)
    });

}


function create(){
    console.log("clicked")
    if($("#intro")[0].files.length ===0 )
    {
        alert("No Intro file selected")
        return
    }
    // if($("#outro")[0].files.length ===0 )
    // {
    //     alert("No Outro file selected")
    //     return
    // }
    // if($("#trans")[0].files.length ===0 )
    // {
    //     alert("No Transition file selected")
    //     return
    // }
    
    // var outro = document.getElementById("outro")
    // var trans = document.getElementById("outro")

    var form_data = new FormData($('#file-form')[0]);
    form_data.append('file_attach', $('input[name=intro]')[0].files[0]);

    console.log(form_data)

    $.ajax({
      url: '/create',
      data: form_data,
      processData: false,
      contentType: false,
      type: 'POST',
      success: function(resp){
        console.log(resp);
      }
  });
    
  

}
           
// const imgsrc = "../images"

// $(".select-window").append(
//     `<img src='../images/1.jpg' style="border-radius:50%">`
// )