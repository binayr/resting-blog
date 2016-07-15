$(document).ready(function() {
    blog.init();
    $('#search-blog-form').on('submit', function(e){
      e.preventDefault();
      blog.search_blog($('#search-feed').val())
    });
    $('#blog-form').on('submit', function(e){
      e.preventDefault();
      console.log('first check')
      blog.create();
    });
});

var Blog = function() {
    this.init = function(){
      var self = this;
      $.ajax({  
          type: "GET",  
          url: '#',
          dataType: "json",
          beforeSend: function(){$(".loader").show()},
          success: function(res) { 
              self.load_blogs(res, 6);
          }  
      }).done(function(){$(".loader").hide()});
    }
    this.load_blogs = function(data, number){
      var html = '';
      if(data.length!=0){
        if(data.length<number){number=data.length}
        for(var i = 0; i < number; i++) {
          html += '<a href="javascript:void(0);" onclick="open_summary('+"'"+data[i].id+"'"+');">\
                  <div class="panel panel-danger col-md-3 col-sm-12 blog-panel">\
                  <div class="panel-heading teal">\
                      <h3 class="panel-title white-text">'+ data[i].title +'</h3>\
                  </div>\
                  <div class="panel-body">\
                      <img class="img-responsive" src="'+data[i].thumbnail+'">\
                  </div>\
                  <span style="padding:10px;">Created by <a href="'+data[i].creator.profile_url+'">@'+ data[i].creator.username +'</a></span>\
              </div></a>';          
        }
      } else {
        html = '<div class="alert alert-dismissible alert-info">\
                  <button type="button" class="close" data-dismiss="alert">×</button>\
                  <strong>OOPs!</strong> No records found.</div>'
      }
      $("#blog-div").html(html);
    }
    this.search_blog = function(title){
      var self = this;
      $("#blog-div").empty();
      $.ajax({  
          type: "GET",  
          url: 'GET_BLOG',
          data: 'title='+title,
          dataType: "json",
          beforeSend: function(){$(".loader").show()},
          success: function(res) {
              self.load_blogs(res, 50)
          }  
      }).done(function(){$(".loader").hide()});
    }
    this.create = function(){
      console.log('second')
      var self = this;
      $("#id_slug").val(self.slugify($('#id_title').val()));
      $.ajax({  
          type: "POST",
          url: $('#blog-form').attr('action'),
          data: $('#blog-form').serialize(),
          dataType: "json",
          beforeSend: function(){$(".loader").show()},
          success: function(res) {
              alert('success');
          }  
      }).done(function(){$(".loader").hide()});      

    }
    this.slugify = function(Text)
    {
        return Text
            .toLowerCase()
            .replace(/ /g,'-')
            .replace(/[^\w-]+/g,'')
            ;
    }
}

var blog = new Blog();