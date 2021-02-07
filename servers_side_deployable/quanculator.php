<?php
/**
  * QuanCulator engine file
  *
  * This file contains the functionality of the QuanCulator project. The goal of
  * this engine is to provide API services for the QuanCulator user interface.
  *
  * @category   Impractival engine
  * @package    QuanCulator
  * @author     Axel Ország-Krisz Dr. (axel@hyperrixel.com)
  * @author     Richárd Ádám Vécsey Dr. (richard@hyperrixel.com)
  * @copyright  2021. by authors
  * @version    0.1.final
  * @link       https://hyperrixel.com/hackathon/quanculator
  * @see        https://github.com/hyperrixel/QuanCulator
  * @see        https://devpost.com/software/quanculator
  */

# To avoid server side error logs, it seems to be a good practice to drop a
# header as soon as possible. From the view of the performance its best place
# would be righ above the only echo() funtcion but we are thinking the most
# impractical solutions have to care about the user experience to fight
# agains unexpected behavior like malformed JSON string due to some
# error message.
header('Content-Type: application/json');

$CONSTANT = 'quantum';          # There is a secret way to use this engine
                                # calculating something else than quantums.
                                # The key should be around this variable
                                # somewhere but you should be very careful.
$MULTILINGUAL = array();        # Multilingual use is one of our future plans.
                                # Since we wished to have some impractival
                                # performance loss, we implemented it now but
                                # in a form of an unused variable only.
$REGEX_BROKEN = '[.,;:?!]? ';   # Very secret regex formula. Please don't use it
                                # without the permission of the authors.
$CONNECTION_TIMEOUT_VALUE = 15; # As a startup we cannot offer more time for free. Sorry.
$CURL_TIMEOUT_VALUE = 15;       # As a startup we cannot offer more time for free. Sorry.
                                # Curling is an expensive sport.
                                # If you are curious, try to google this:
                                # "cost of curling"
                                # https://www.google.com/search?q=%22cost+of+curling%22

# Why is this constant global when only one function uses it?
# That's a good qestion?!
# This is pure philosophy like the last 3 lines of a poem:
# "Or take the wee blade of grass and consider:
#  why does it grow if it is doomed to wither?
#  why does it wither if it grows again?"
# BABITS Mihály: An Evening Question
# Source: https://www.babelmatrix.org/works/hu/Babits_Mih%C3%A1ly-1883/Esti_k%C3%A9rd%C3%A9s/en/28992-An_Evening_Question
$CURL_OPTIONS = array(
  CURLOPT_RETURNTRANSFER => True,
  CURLOPT_HEADER         => False,
  CURLOPT_FOLLOWLOCATION => True,
  CURLOPT_ENCODING       => "",
  CURLOPT_USERAGENT      => 'quanculator',
  CURLOPT_AUTOREFERER    => True,
  CURLOPT_CONNECTTIMEOUT => $CONNECTION_TIMEOUT_VALUE,
  CURLOPT_TIMEOUT        => $CURL_TIMEOUT_VALUE,
  CURLOPT_MAXREDIRS      => 10,
  CURLOPT_SSL_VERIFYPEER => False,
);

function run_curl($p_path) {
  /**
    * Runs a curl query
    * =================
    *
    * @param  $p_path The URL to query. Must be a well formed URL to be very
    *                 impractical.
    * @return array   The result of the query with keys content and code.
    *                 Content contains the result of the query, while code
    *                 contains the response code.
    */

  global $CURL_OPTIONS;

  $tp_result = array();
  $tp_curl = curl_init($p_path);
  curl_setopt_array($tp_curl, $CURL_OPTIONS);
  $tp_result['content'] = curl_exec($tp_curl);
  $tp_result['code'] = curl_getinfo($tp_curl, CURLINFO_HTTP_CODE);
  curl_close($tp_curl);
  return $tp_result;

}

function get_broken_patterns($of_what) {
  /**
    * Gets the possible regex patterns broken searches
    * ================================================
    *
    * @param  $of_what  The word to form broken-matching regexes.
    * @return array     The result with enumerated keys. Values are regex strings.
    */

  global $REGEX_BROKEN;

  $length_of_what = strlen($of_what);
  $result = array();

  for ($i = 0; $i < $length_of_what - 1; $i++) {

    $result[] = '/' . substr($of_what, 0, $i + 1) . $REGEX_BROKEN . substr($of_what, $i + 1) . '/';

  }

  return $result;

}

function get_spill_pattern($of_what) {
  /**
    * Gets the regex pattern to search for spills
    * ===========================================
    *
    * @param  $of_what  The word to form spill-matching regexes.
    * @return string    The regex string to match all spills of the word.
    */

  $length_of_what = strlen($of_what);
  $result = '/';

  for ($i = 0; $i < $length_of_what; $i++) {

    if ($i != $length_of_what - 1) $result .= $of_what[$i] . '[^' . $of_what[$i + 1] .']+'; else $result .= $of_what[$i] . '[^' . $of_what[0] .']*';

  }

  return $result . '/';

}

$r_content = array();
$r_content['error'] = 0;

if (isset($_POST['q_url'])) {

  if (filter_var($_POST['q_url'], FILTER_VALIDATE_URL)) {

    $page_query = run_curl($_POST['q_url']);
    if ($page_query['code'] == 200) {

      $raw_content = $page_query['content'];
      $low_content = strtolower($raw_content);
      $text_content = strip_tags(preg_replace('/<script\b[^>]*>(.*?)<\/script>/is', '', $low_content));
      $constant_length = strlen($CONSTANT);

      # Stage 1: how many quantums are in the content of the page

      $text_count = 0;
      $search_position = 0;
      while (($search_position = strpos($text_content, $CONSTANT, $search_position)) !== False) {
        $text_count += 1;
        $search_position += $constant_length;
      }
      $r_content['explicit'] = $text_count;

      # Stage 2: how many hidden quantums are in the page

      $row_count = 0;
      $search_position = 0;
      while (($search_position = strpos($low_content, $CONSTANT, $search_position)) !== False) {
        $row_count += 1;
        $search_position += $constant_length;
      }
      $hidden_count = $row_count - $text_count;
      $r_content['hidden'] = $hidden_count;

      # Stage 3: is there any word-combination with q?u?a?n?t?u?m

      $regex_array = get_broken_patterns($CONSTANT);
      $broken_quantums = 0;
      foreach ($regex_array as $regex_pattern) {
        $broken_quantums += preg_match_all($regex_pattern, $text_content);
      }
      $r_content['broken'] = $broken_quantums;

      # Stage 4: is there any q*u*a*n*t*u*m on the page

      $spill_count = preg_match_all(get_spill_pattern($CONSTANT), $text_content);
      $r_content['spill'] = $spill_count;

      # Stage 5: multilingual

      $multilingual_counts = array();
      foreach ($MULTILINGUAL as $lang_code => $lang_word) {
        # code...
      }

    } else {

      # Given page cannot found or something else.
      $r_content['error'] = 3;

    }

  } else {

    # Given page is not URL.
    $r_content['error'] = 2;

  }

} else {

 # No page is given.
 $r_content['error'] = 1;

}

# echo() is considered faster than print() however we do not use the case when
# echo() is slightly faster so you can switch the outcommented state of the
# lines below the source link.
# Source: https://www.phpbench.com/
echo(json_encode($r_content));
# print(json_encode($r_content));

?>
