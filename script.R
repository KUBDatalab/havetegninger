

hent_have_data <- function(){
  url <- "http://www5.kb.dk/images/billed/2010/okt/billeder/subject37894/da/?page="
  data <- httr::GET(paste0(url,1), add_headers(Accept = "application/json")) %>% 
    content(type = "text", encoding = "UTF-8") %>% 
    fromJSON()
  data <- data$response
  sider <- data$pages$total_pages
  res <- list()
  res[[1]] <- data$docs %>% as.data.frame()
  for(i in 2:sider){
    res[[i]] <- httr::GET(paste0(url,i), add_headers(Accept = "application/json")) %>% 
      content(type = "text", encoding = "UTF-8") %>% fromJSON() %>% 
      .$response %>% 
      .$docs %>% 
      as.data.frame()
  }
  bind_rows(res)
}

test <- hent_have_data()
test %>% 
  select(-cataloging_language_ssi,
         -title_tdsim,
         -author_tsim,
         -author_nasim,
         -medium_ssi,
         -creator_ssi,
         -creator_display_tsim,
         -creator_tsim,
         -creator_nasim,
         -format_tsim,
         -rights_tsim,
         -type_tsim,
         -pub_dat_tsi,
         -pub_dat_display_tsi,
         -readable_dat_string_tsim,
         -content_metadata_image_iiif_info_ssm,
         -subject_topic_id_ssim,
         -subject_topic_facet_tesim,
         -subject_topic_facet_tdsim,
         -description_tsim,
         -mods_ts,
         -ese_type_tsim,
         -ese_rights_tsim,
         -ese_dataProvider_tsim,
         -local_id_fngsi,
         -cobject_correctness_isi,
         -cobject_interestingness_isi,
         -score,
         -dc_type_ssim,
         -dc_type_tdsim,
         -timestamp,
         -`_version_`,
         -cumulus_catalog_ssi,
         -cobject_last_modified_by_ssi,
         -cobject_title_ssi,
         -cobject_random_number_dbsi,
         -cobject_not_after_dtsi,
         -cobject_not_before_dtsi,
         -cobject_last_modified_lsi,
         -processed_mods_ts) %>% 
  filter(str_detect(full_title_tsi, "lufthavn")) 




