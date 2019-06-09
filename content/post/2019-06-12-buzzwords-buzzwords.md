---
title: 'Buzzwords buzzwords'
date: 2019-06-12 10:00:00 +0000
feature_image: "/uploads/words.jpg"
tags:
- tecnology
- buzzword
- buzzwords
categories:
- dev
slug: buzzwords-buzzwords
description: Un rant sulle buzzwords

---
Test {{< buzzword >}}

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
  $(function () {
    count = 0;
    wordsArray = ["Big data", "Blockchain", "Cloud", "Cross-platform", "Deep learning", "DevOps",
      "Machine Learning", "Microservices", "Real-time", "Scalability", "Think outside the box", "Web 2.0",
      "Wev 3.0"
    ];
    setInterval(function () {
      count++;
      $(".buzzword").fadeOut(400, function () {
        $(this).text(wordsArray[count % wordsArray.length]).fadeIn(400);
      });
    }, 2000);
  });
</script>
