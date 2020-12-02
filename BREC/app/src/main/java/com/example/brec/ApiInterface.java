package com.example.brec;

import com.example.brec.model.Book;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Headers;
import retrofit2.http.Query;

public interface ApiInterface {
    @Headers({"X-Naver-Client-Id: a7NttKjlK1OGDVHhZtsC", "X-Naver-Client-Secret: DbPnppu4Pw"})
    @GET("book.json")
    Call<Book> getBooks(@Query("query") String title,
                         @Query("display") int displaySize,
                         @Query("start") int startPosition);
}
